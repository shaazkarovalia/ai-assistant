import streamlit as st
from groq import Groq

def initialize_groq_client():
    try:
        api_key = st.secrets["GROQ_API_KEY"]
        client = Groq(api_key=api_key)
        return client
    except Exception as e:
        st.error("⚠️ API Key missing! Please check `.streamlit/secrets.toml`.")
        st.stop()

def get_ai_response_stream(client, messages, model="llama-3.3-70b-versatile"):
    """
    Ye function Groq API ko call karega aur response ko tukdon (chunks) me wapas karega.
    """
    try:
        stream = client.chat.completions.create(
            model=model,
            messages=[{"role": m["role"], "content": m["content"]} for m in messages],
            stream=True,
        )
        for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
    except Exception as e:
        yield f"Error: {str(e)}"