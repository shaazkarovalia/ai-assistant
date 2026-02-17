# 🤖 High-Performance Modular Chatbot

A professional-grade AI Chat Assistant built with **Streamlit** and powered by **Groq’s Llama 3.3 (70B) model**. This project focuses on high-speed streaming, modular software architecture, and a custom-engineered mobile-responsive UI.

## 🌟 Key Features

* **Ultra-Fast Inference:** Leverages the Groq API and Llama-3.3-70B-Versatile model to deliver sub-second response times.
* **Real-Time Streaming:** Implements Python generator functions (`yield`) for a "typewriter" effect, significantly reducing perceived latency.
* **Mobile-First Design:** Features a custom CSS Flexbox architecture that keeps prompt cards horizontal even on small screens, bypassing default Streamlit limitations.
* **Modular Architecture:** Structured into decoupled layers—`app.py` (Controller), `ui.py` (View), and `logic.py` (Model)—for maximum maintainability and scalability.
* **Intelligent State Management:** Uses Streamlit's `session_state` to handle persistent chat history and asynchronous card triggers across reruns.

## 🛠️ Tech Stack

* **Language:** Python
* **Frontend:** Streamlit + Custom CSS3 (Flexbox/Grid)
* **LLM Model:** Llama 3.3 (70B Parameters)
* **API Inference:** Groq Cloud

## 📁 Project Structure

```text
ai-assistant/
├── app.py          # Main Controller: Manages state and application flow
├── ui.py           # UI Layer: Custom CSS styling and landing page layout
├── logic.py        # Logic Layer: API initialization and streaming response generator
├── .streamlit/
│   └── secrets.toml# Configuration: Secure API key storage
└── requirements.txt# Dependencies: Streamlit, Groq, etc.
