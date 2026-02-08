import requests
import json

OLLAMA_URL = "http://localhost:11434/api/chat"

def chat_with_model(model_name: str, messages: list, stream: bool = True):
    payload = {
        "model": model_name,
        "messages": messages,
        "stream": stream
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        stream=stream,
        timeout=300
    )

    if not stream:
        return response.json()["message"]["content"]

    # Streaming response (ChatGPT-like)
    full_reply = ""
    for line in response.iter_lines():
        if not line:
            continue

        data = json.loads(line.decode("utf-8"))

        if "message" in data and "content" in data["message"]:
            chunk = data["message"]["content"]
            print(chunk, end="", flush=True)
            full_reply += chunk

        if data.get("done"):
            break

    print()  # newline after stream
    return full_reply
