from flask import Flask, jsonify, request

from llm_gateway import ask_llm

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/api/ask", methods=["POST"])
def ask():
    body = request.get_json(silent=True)
    if not body or not body.get("prompt"):
        return jsonify({"ok": False, "error": "Field 'prompt' is required."}), 400

    result = ask_llm(
        prompt=body["prompt"],
        system_prompt=body.get("system_prompt", "You are a helpful assistant."),
        model_kwargs=body.get("model_kwargs"),
        response_schema=body.get("response_schema"),
        enforce_json=body.get("enforce_json", True),
    )

    status_code = 200 if result["ok"] else 502
    return jsonify(result), status_code


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)