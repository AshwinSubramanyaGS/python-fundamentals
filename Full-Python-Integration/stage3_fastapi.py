from typing import Any, Dict, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from llm_gateway import ask_llm

app = FastAPI(title="Reusable LLM Gateway API", version="1.0.0")


class ModelKwargs(BaseModel):
    maxTokens: int = Field(default=2000, ge=1, le=8192)
    temperature: float = Field(default=0.3, ge=0.0, le=2.0)
    topP: float = Field(default=0.9, ge=0.0, le=1.0)
    streaming: bool = False


class AskRequest(BaseModel):
    prompt: str = Field(..., min_length=1, examples=["Give me 3 highlights about Bangalore."])
    system_prompt: str = Field(
        default="You are a concise analyst. Return clean JSON.",
        examples=["Return JSON with keys: topic, summary, highlights."],
    )
    model_kwargs: ModelKwargs = Field(default_factory=ModelKwargs)
    response_schema: Optional[Dict[str, Any]] = None
    enforce_json: bool = True


class AskResponse(BaseModel):
    ok: bool
    provider: str
    model: str
    data: Optional[Any] = None
    raw_text: str
    error: Optional[str] = None


@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "healthy"}


@app.post("/api/ask", response_model=AskResponse)
def ask_endpoint(req: AskRequest) -> Dict[str, Any]:
    result = ask_llm(
        prompt=req.prompt,
        system_prompt=req.system_prompt,
        model_kwargs=req.model_kwargs.model_dump(),
        response_schema=req.response_schema,
        enforce_json=req.enforce_json,
    )
    if not result["ok"]:
        raise HTTPException(status_code=502, detail=result["error"])
    return result