import streamlit as st
import ui 
import logic 

st.set_page_config(
    page_title="Shaaz's AI Assistant",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

ui.apply_custom_styling()
client = logic.initialize_groq_client()

if "messages" not in st.session_state:
    st.session_state.messages = []
if "prompt_clicked" not in st.session_state:
    st.session_state.prompt_clicked = None

# Landing UI logic
if not st.session_state.messages:
    ui.show_landing_page()

# Chat Display
for message in st.session_state.messages:
    avatar = "🧑‍💻" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Input
user_input = st.chat_input("Message Chat...")

if st.session_state.prompt_clicked:
    st.session_state.messages.append({"role": "user", "content": st.session_state.prompt_clicked})
    st.session_state.prompt_clicked = None
    st.rerun()
elif user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("assistant", avatar="🤖"):
        res = st.write_stream(logic.get_ai_response_stream(client, st.session_state.messages))
        st.session_state.messages.append({"role": "assistant", "content": res})
    st.rerun()