import json

from llm_gateway import ask_llm

# --- Customize these 3 blocks for any use case ---
SYSTEM_PROMPT = (
    "You are a concise domain analyst. Always return structured, factual JSON "
    "matching the requested schema."
)

USER_PROMPT = "Give me 3 highlights about Bangalore."

RESPONSE_SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "topic": {"type": "STRING"},
        "summary": {"type": "STRING"},
        "highlights": {
            "type": "ARRAY",
            "items": {"type": "STRING"},
        },
    },
    "required": ["topic", "summary", "highlights"],
}

MODEL_KWARGS = {
    "maxTokens": 1000,
    "temperature": 0.3,
    "topP": 0.9,
    "streaming": False,
}


def main() -> None:
    result = ask_llm(
        prompt=USER_PROMPT,
        system_prompt=SYSTEM_PROMPT,
        model_kwargs=MODEL_KWARGS,
        response_schema=RESPONSE_SCHEMA,
        enforce_json=True,
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()