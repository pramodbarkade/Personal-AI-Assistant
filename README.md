# 🧠 Personal AI Assistant (Local, Free, No API Keys)

A **fully local, ChatGPT-like AI assistant** built using **Ollama** and **open-source models**.
Runs on your own machine, **100% free**, with both **Python agent** and **Web UI** support.

No cloud.
No API keys.
No billing.

---

## ✨ Features

* ✅ Runs **entirely locally**
* ✅ **ChatGPT-like live streaming** responses
* ✅ **Web UI (HTML)** – no backend required
* ✅ **Python AI agent** for automation & tools
* ✅ **Multiple models supported**
* ✅ **Model dropdown with install detection**
* ✅ **Single shared configuration (`models.json`)**
* ✅ Works offline (after model download)

---

## 🏗 Architecture Overview

```
              ┌───────────────────┐
              │      Ollama       │
              │  (Local AI Host)  │
              └─────────┬─────────┘
                        │
        ┌───────────────┼───────────────┐
        │                                   │
┌──────────────┐                 ┌──────────────┐
│ Python Agent │                 │   Web UI     │
│ ai_agent.py  │                 │   ui.html    │
└──────────────┘                 └──────────────┘
```

* **Ollama** runs the AI models
* **Python agent** and **Web UI** are just clients
* Both talk to the same local AI engine

---

## 📁 Project Structure

```
Personal-AI-Assistant/
│
├── config/
│   └── models.json        # Central model configuration
│
├── src/
│   ├── ai_agent.py        # Python CLI AI agent
│   └── llm/
│       ├── model_config.py
│       └── ollama_client.py
│
├── ui.html                # Web UI (ChatGPT-like)
├── README.md
└── requirements.txt
```

---

## 🧠 Supported Models (Free)

| Model          | Category          | RAM    | Notes                   |
| -------------- | ----------------- | ------ | ----------------------- |
| **Phi-3 Mini** | Fast Chat         | ~4 GB  | Default, best balance   |
| **Mistral 7B** | High Quality Text | ~6 GB  | Better reasoning & code |
| **TinyLLaMA**  | Lightweight       | ~2 GB  | Low-resource fallback   |
| **Qwen 1.5B**  | Small but Smart   | ~3 GB  | Strong for size         |
| **LLaVA 7B**   | Vision (Optional) | ~10 GB | Image + text            |

> You can add/remove models easily via `config/models.json`.

---

## ⚙️ Prerequisites

* **OS:** Windows / macOS / Linux
* **RAM:** 8 GB minimum (16 GB recommended)
* **Python:** 3.10+
* **Internet:** Only for first model download

---

## 🚀 Step-by-Step Setup

### 1️⃣ Install Ollama

Download and install Ollama:

👉 [https://ollama.com/download](https://ollama.com/download)

Verify:

```bash
ollama --version
```

---

### 2️⃣ Download a Model (Recommended)

```bash
ollama pull phi3:mini
```

Optional (better quality):

```bash
ollama pull mistral
```

Verify:

```bash
ollama list
```

---

### 3️⃣ Run the Python AI Agent

```bash
python src/ai_agent.py
```

Features:

* CLI chat
* Model switching
* Streaming output

---

### 4️⃣ Run the Web UI

Start a lightweight local server:

```bash
python -m http.server 8000
```

Open in browser:

```
http://localhost:8000/ui.html
```

✔ Model dropdown
✔ Disabled models if not installed
✔ Live typing responses

---

## ⚙️ Central Model Configuration

All models are defined in **one place**:

```
config/models.json
```

Both:

* Python agent
* Web UI

read from the same config.

This ensures:

* No duplication
* Consistent defaults
* Easy maintenance

---

## 🔒 Privacy & Cost

* 🔐 Data never leaves your machine
* 💰 Cost = **₹0 / $0**
* 🔑 No API keys
* 📡 No cloud dependency

---

## 🎥 Perfect for Demos & Learning

This project is ideal for:

* YouTube tutorials
* AI agent demos
* Local AI experimentation
* Learning system design
* Offline AI usage

---

## 🛣 Roadmap (Optional)

* Conversation memory
* Tool usage (files, commands)
* Vision UI (image upload)
* Backend API (FastAPI)
* Deployment mode

---

## 📜 License

This project uses **open-source models**.
Please follow the individual model licenses when redistributing.

---

## 🙌 Author

Built for learning, demos, and community sharing.
Feel free to fork, extend, and improve.

---

### ⭐ If this helped you

Give the repo a star and share it with others building local AI 🚀