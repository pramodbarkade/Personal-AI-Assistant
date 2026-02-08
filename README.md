# 🧠 Personal AI Assistant

**Local AI • ChatGPT-like • No API Keys • 100% Free**

A **fully local, open-source AI assistant** built using **Ollama**, **modern open LLMs**, and a clean **Python + Web UI** architecture.

This project is a **ChatGPT alternative that runs entirely on your machine**.
No cloud. No billing. No API keys. Full privacy.

---

## 🔖 Version

**v1.0 – Stable Demo Release**

---

## ✨ Key Features

* ✅ **Runs 100% locally** (offline after setup)
* ✅ **ChatGPT-like streaming responses**
* ✅ **Web UI (HTML only)** – no backend required
* ✅ **Python CLI AI Agent**
* ✅ **Multiple local LLMs supported**
* ✅ **Model dropdown with auto-detection**
* ✅ **Single shared configuration (`models.json`)**
* ✅ Free, private, and open-source

---

## 📸 Screenshots

### 🖥️ Web UI – ChatGPT-like Interface (Local & Free)
![Local AI Web UI](./screenshots/web-ui.png)

A clean browser-based interface with:
- Live streaming responses
- Model dropdown with availability status
- Default model auto-selection
- No backend or API keys

---

### 🧪 Python CLI – AI Agent in Action
![Python AI Agent CLI](./screenshots/python-cli.png)

Command-line AI agent featuring:
- Streaming responses
- Model switching
- Fully local execution via Ollama

---

## 🔍 Why This Project?

If you’re looking for:

* a **local ChatGPT alternative**
* an **offline AI assistant**
* a **free AI agent using Python**
* an **Ollama-based LLM demo**
* a **browser-based AI UI without APIs**

This project is for you.

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

* **Ollama** hosts and runs the LLMs locally
* **Python agent** and **Web UI** are independent clients
* Both use the **same local AI engine**
* Clean separation, no duplication

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
├── ui.html                # ChatGPT-like Web UI
├── README.md
├── .gitignore
└── requirements.txt
```

---

## 🧠 Supported Local LLM Models (Free & Offline)

| Model          | Category            | Approx RAM | Use Case                        |
| -------------- | ------------------- | ---------- | ------------------------------- |
| **Phi-3 Mini** | Fast Chat (Default) | ~4 GB      | Best balance of speed & quality |
| **Mistral 7B** | High-Quality Text   | ~6 GB      | Better reasoning & coding       |
| **TinyLLaMA**  | Ultra-Light         | ~2 GB      | Low-resource systems            |
| **Qwen 1.5B**  | Small but Smart     | ~3 GB      | Efficient reasoning             |
| **LLaVA 7B**   | Vision (Optional)   | ~10 GB     | Image + text (experimental)     |

All models are **free, local, and configurable** via `config/models.json`.

---

## ⚙️ System Requirements

* **OS:** Windows / macOS / Linux
* **RAM:** 8 GB minimum (16 GB recommended)
* **Python:** 3.10 or higher
* **Internet:** Only required for first model download

---

## 🚀 Getting Started (Step-by-Step)

### 1️⃣ Install Ollama

Download and install Ollama:
👉 [https://ollama.com/download](https://ollama.com/download)

Verify installation:

```bash
ollama --version
```

---

### 2️⃣ Download a Local Model

Recommended default:

```bash
ollama pull phi3:mini
```

Optional (better quality):

```bash
ollama pull mistral
```

Verify installed models:

```bash
ollama list
```

---

### 3️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Python AI Agent

```bash
python src/ai_agent.py
```

You get:

* CLI chat
* Streaming responses
* Model switching
* Fully local execution

---

### 5️⃣ Run the Web UI (Browser-based ChatGPT-like Interface)

Start a lightweight local server:

```bash
python -m http.server 8000
```

Open in browser:

```
http://localhost:8000/ui.html
```

Web UI features:

* Model dropdown
* Disabled models if not installed
* Default model auto-selected
* Live streaming replies

---

## ⚙️ Central Model Configuration

All models are managed in **one place**:

```
config/models.json
```

This file is shared by:

* Python AI agent
* Web UI

Benefits:

* Single source of truth
* Easy to add/remove models
* Consistent behavior across interfaces

---

## 🔒 Privacy & Cost

* 🔐 Your data **never leaves your machine**
* 💰 Cost = **₹0 / $0**
* 🔑 No API keys
* ☁️ No cloud dependency

---

## 🚧 Known Limitations

* Models are **text-only by default**
* Vision models (LLaVA) are heavier and optional
* Web UI requires a local HTTP server
* Ollama must be running in the background

---

## 🛣 Roadmap

* Conversation memory
* Tool usage (files, commands, automation)
* Vision UI (image upload)
* Optional backend API (FastAPI)
* Deployment / multi-device mode

---

## ❓ FAQ

**Is this completely free?**
Yes. All models run locally using Ollama.

**Does this require internet access?**
Only for the first model download.

**Is my data private?**
Yes. Everything stays on your machine.

**Is this a ChatGPT replacement?**
For many local, offline, and privacy-focused use cases, yes.

---

## 🎥 Video Tutorial

A full **step-by-step YouTube walkthrough** is planned, covering:

* Installing Ollama
* Running local LLMs
* Python AI agent
* Web-based ChatGPT-like UI
* Model comparisons

(YouTube link will be added here.)

---

## 📜 License

This project uses **open-source models via Ollama**.
Please review individual model licenses before redistribution.

---

## 🙌 Author

Created by **Pramod Barkade**
Built for learning, demos, and the open-source AI community.

---

⭐ If this project helps you, **star the repository** and share it.

<!--
Keywords: local ai assistant, chatgpt alternative, ollama ai, offline ai, free ai assistant, python ai agent, local llm ui
-->