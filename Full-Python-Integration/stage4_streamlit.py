import json

import streamlit as st

from llm_gateway import ask_llm

st.set_page_config(page_title="LLM Gateway Workbench", layout="wide")
st.title("Reusable LLM Gateway Workbench")

# Sidebar: Model Kwargs & JSON Controls
with st.sidebar:
    st.header("Model Parameters (modelKwargs)")
    temperature = st.slider("temperature", 0.0, 2.0, 0.3, 0.1)
    top_p = st.slider("topP", 0.0, 1.0, 0.9, 0.05)
    max_tokens = st.number_input("maxTokens", min_value=100, max_value=8192, value=1500, step=100)
    enforce_json = st.checkbox("Enforce JSON Output", value=True)

    default_schema = json.dumps(
        {
            "type": "OBJECT",
            "properties": {
                "topic": {"type": "STRING"},
                "summary": {"type": "STRING"},
                "highlights": {"type": "ARRAY", "items": {"type": "STRING"}},
            },
            "required": ["topic", "summary", "highlights"],
        },
        indent=2,
    )
    schema_text = st.text_area("Optional JSON Schema (Gemini REST)", value=default_schema, height=240)

# Main Panel: System & User Prompts
system_prompt = st.text_area(
    "System Prompt",
    value="You are a concise analyst. Return accurate, structured JSON.",
    height=90,
)
user_prompt = st.text_area(
    "User Prompt",
    value="Give me 3 highlights about Bangalore.",
    height=120,
)

if st.button("Send Request", type="primary"):
    if not user_prompt.strip():
        st.warning("Please enter a user prompt.")
        st.stop()

    parsed_schema = None
    if enforce_json and schema_text.strip():
        try:
            parsed_schema = json.loads(schema_text)
        except json.JSONDecodeError as exc:
            st.error(f"Invalid JSON Schema: {exc}")
            st.stop()

    with st.spinner("Calling LLM Gateway..."):
        result = ask_llm(
            prompt=user_prompt,
            system_prompt=system_prompt,
            model_kwargs={
                "temperature": temperature,
                "topP": top_p,
                "maxTokens": int(max_tokens),
                "streaming": False,
            },
            response_schema=parsed_schema,
            enforce_json=enforce_json,
        )

    if result["ok"]:
        st.success(f"Success via {result['provider']} ({result['model']})")
        if result["data"] is not None:
            st.subheader("Parsed JSON Response")
            st.json(result["data"])
        else:
            st.subheader("Text Response")
            st.write(result["raw_text"])
    else:
        st.error(f"Request failed: {result['error']}")

    with st.expander("Inspect Full Normalized Envelope"):
        st.json(result)