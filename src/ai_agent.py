from llm.model_config import MODELS, DEFAULT_MODEL
from llm.ollama_client import chat_with_model

def main():
    current_model_key = DEFAULT_MODEL
    current_model = MODELS[current_model_key]

    system_prompt = (
        "You are a helpful, professional personal AI assistant. "
        "Be clear, concise, and practical."
    )

    messages = [
        {"role": "system", "content": system_prompt}
    ]

    print("\n✨ PB | Free Local AI Agent ✨")
    print(f"Using model: {current_model_key}")
    print("Type 'models' to list models, 'use <name>' to switch, 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ("quit", "exit"):
            print("Assistant: Goodbye 👋")
            break

        if user_input.lower() == "models":
            print("\nAvailable models:")
            for key, cfg in MODELS.items():
                marker = " (default)" if key == DEFAULT_MODEL else ""
                print(f"- {key}{marker}: {cfg['description']}")
            print()
            continue

        if user_input.lower().startswith("use "):
            model_key = user_input.split(" ", 1)[1].strip()
            if model_key in MODELS:
                current_model_key = model_key
                current_model = MODELS[model_key]
                print(f"🔄 Switched to model: {model_key}\n")
            else:
                print("❌ Unknown model key\n")
            continue

        messages.append({"role": "user", "content": user_input})

        print("Assistant: ", end="", flush=True)
        reply = chat_with_model(
            model_name=current_model["id"],
            messages=messages,
            stream=True
        )

        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
