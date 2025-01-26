# 🚀 Personal LLM Chat Assistant

A 100% local, privacy-focused AI chatbot powered by **DeepSeek-R1**, **Ollama**, and **Chainlit**. This project allows you to run a personal large language model (LLM) on your machine without relying on external APIs.


---

## ✨ Features

- 🔒 **Privacy First**: Runs entirely on your machine—no data leaves your device.
- 💻 **Local Execution**: Powered by Ollama for local LLM serving.

---

## 🛠️ Setup Guide

### Prerequisites
- **Python 3.8+**
- **Ollama** installed and running
- **DeepSeek-R1 model** downloaded
- **Git** (for cloning the repository)

---

### Step 1: Clone the Repository

```bash
git clone https://github.com/VAmanjain/Assistant
cd Assistant
```



### Step 2: Set Up Python Environment
Create a virtual environment:
```bash
Copy
python -m venv venv
Activate the environment:
```
Windows:
```bash
venv\Scripts\activate
```
Linux/macOS:

```bash
source venv/bin/activate
```

### Step 3: Install and Set Up Ollama
1. Install Ollama:

Windows: Download from [Ollama's website](https://ollama.com/).

Linux/macOS:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```
Download DeepSeek-R1 Model:

```bash
ollama pull deepseek-r1
```

Start Ollama Server:

```bash
ollama serve
```

### Step 4: Run the Chat Interface
Start the Chainlit server:

```Copy
chainlit run deepseek_chat.py -w
```
Open your browser and navigate to:

```
http://localhost:8000
```

## 🙏 Acknowledgments
DeepSeek for the LLM model.

Ollama for local model serving.

Chainlit for the beautiful chat interface.
