import json
import os
import re
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv(override=True)

DEFAULT_MODEL_KWARGS: dict[str, Any] = {
    "maxTokens": 2000,
    "temperature": 0.3,
    "topP": 0.9,
    "streaming": False,
}


def _parse_json_safely(raw_text: str) -> Any | None:
    """Parse JSON directly, with fallback stripping for markdown code fences."""
    cleaned = raw_text.strip()
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        match = re.search(r"```(?:json)?\s*(.*?)\s*```", cleaned, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1))
            except json.JSONDecodeError:
                return None
        return None


def _call_gemini_rest(
    prompt: str,
    system_prompt: str,
    model: str,
    kwargs: dict[str, Any],
    enforce_json: bool,
    response_schema: dict[str, Any] | None,
) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Missing GEMINI_API_KEY in .env")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": api_key,
    }

    generation_config: dict[str, Any] = {
        "maxOutputTokens": kwargs.get("maxTokens", 2000),
        "temperature": kwargs.get("temperature", 0.3),
        "topP": kwargs.get("topP", 0.9),
    }

    if enforce_json:
        generation_config["responseMimeType"] = "application/json"
        if response_schema:
            generation_config["responseSchema"] = response_schema

    payload: dict[str, Any] = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": generation_config,
    }

    if system_prompt:
        payload["systemInstruction"] = {"parts": [{"text": system_prompt}]}

    resp = requests.post(url, headers=headers, json=payload, timeout=30)
    resp.raise_for_status()
    body = resp.json()

    candidates = body.get("candidates", [])
    if not candidates:
        raise RuntimeError(f"No candidates returned: {body}")

    parts = candidates[0].get("content", {}).get("parts", [])
    return "".join(part.get("text", "") for part in parts)


def _call_custom_gateway(
    prompt: str,
    system_prompt: str,
    model: str,
    kwargs: dict[str, Any],
    enforce_json: bool,
) -> str:
    gateway_url = os.getenv("GATEWAY_URL")
    gateway_key = os.getenv("GATEWAY_API_KEY")
    backend_provider = os.getenv("GATEWAY_BACKEND_PROVIDER", "bedrock")

    if not gateway_url:
        raise ValueError("Missing GATEWAY_URL in .env")

    effective_system = system_prompt
    if enforce_json:
        effective_system = (
            f"{system_prompt}\nRespond ONLY with valid raw JSON. Do not include prose or markdown fences."
        ).strip()

    # Standard enterprise gateway envelope
    payload = {
        "action": "run",
        "modelInterface": "langchain",
        "data": {
            "mode": "chain",
            "text": prompt,
            "files": [],
            "modelName": model,
            "provider": backend_provider,
            "systemPrompt": effective_system,
            "modelKwargs": {
                "maxTokens": kwargs.get("maxTokens", 2000),
                "temperature": kwargs.get("temperature", 0.3),
                "topP": kwargs.get("topP", 0.9),
                "streaming": kwargs.get("streaming", False),
            },
        },
    }

    headers = {"Content-Type": "application/json"}
    if gateway_key:
        headers["Authorization"] = f"Bearer {gateway_key}"

    resp = requests.post(gateway_url, headers=headers, json=payload, timeout=30)
    resp.raise_for_status()
    body = resp.json()

    # Adjust key path if your gateway uses a specific response wrapper
    if isinstance(body, dict):
        data_block = body.get("data")
        if isinstance(data_block, dict) and "content" in data_block:
            return str(data_block["content"])
        for key in ("output", "response", "text", "content"):
            if key in body:
                return str(body[key])
    return json.dumps(body)


def ask_llm(
    prompt: str,
    system_prompt: str = "You are a helpful assistant.",
    model_kwargs: dict[str, Any] | None = None,
    response_schema: dict[str, Any] | None = None,
    enforce_json: bool = True,
) -> dict[str, Any]:
    """
    Model-agnostic entry point reused across CLI, Flask, FastAPI, and Streamlit.
    """
    provider = os.getenv("LLM_PROVIDER", "gemini").lower()
    model = os.getenv("LLM_MODEL", "gemini-3.8-flash")
    merged_kwargs = {**DEFAULT_MODEL_KWARGS, **(model_kwargs or {})}

    try:
        if provider == "gemini":
            raw_text = _call_gemini_rest(
                prompt=prompt,
                system_prompt=system_prompt,
                model=model,
                kwargs=merged_kwargs,
                enforce_json=enforce_json,
                response_schema=response_schema,
            )
        elif provider == "custom_gateway":
            raw_text = _call_custom_gateway(
                prompt=prompt,
                system_prompt=system_prompt,
                model=model,
                kwargs=merged_kwargs,
                enforce_json=enforce_json,
            )
        else:
            raise ValueError(f"Unsupported LLM_PROVIDER: {provider}")

        parsed = _parse_json_safely(raw_text) if enforce_json else None

        if enforce_json and parsed is None:
            return {
                "ok": False,
                "provider": provider,
                "model": model,
                "data": None,
                "raw_text": raw_text,
                "error": "Model response was not valid JSON.",
            }

        return {
            "ok": True,
            "provider": provider,
            "model": model,
            "data": parsed,
            "raw_text": raw_text,
            "error": None,
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "ok": False,
            "provider": provider,
            "model": model,
            "data": None,
            "raw_text": "",
            "error": str(exc),
        }