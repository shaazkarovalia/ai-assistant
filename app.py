import streamlit as st
import ui 
import logic 

# --- 1. CONFIGURATION (Must be first) ---
st.set_page_config(
    page_title="Shaaz's AI Assistant",
    page_icon="🤖",
    layout="centered", # Isse mobile aur laptop dono pe content center rahega
    initial_sidebar_state="collapsed"
)

# --- 2. SETUP & STATE ---
ui.apply_custom_styling()
client = logic.initialize_groq_client()

if "messages" not in st.session_state:
    st.session_state.messages = []
if "prompt_clicked" not in st.session_state:
    st.session_state.prompt_clicked = None

# --- 3. MAIN FLOW ---

# AGAR HISTORY KHALI HAI -> Landing Page dikhao
if not st.session_state.messages:
    ui.show_header()
    ui.show_prompt_cards()
else:
    # Agar chat shuru ho gayi hai, toh landing page ka code skip ho jayega
    pass

# --- 4. CHAT HISTORY DISPLAY ---
# Ye history hamesha render hogi, landing page ke neeche ya top par
for message in st.session_state.messages:
    avatar = "🧑‍💻" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# --- 5. INPUT HANDLING ---
user_input = st.chat_input("Message Chat...")

# Case A: Agar kisi ne Prompt Card par click kiya
if st.session_state.prompt_clicked:
    current_prompt = st.session_state.prompt_clicked
    st.session_state.prompt_clicked = None # Reset
    st.session_state.messages.append({"role": "user", "content": current_prompt})
    st.rerun() # Refresh taaki landing page foran gayab ho jaye

# Case B: Agar user ne manually type kiya
elif user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("assistant", avatar="🤖"):
        # Logic file se response stream le rahe hain
        response_stream = logic.get_ai_response_stream(client, st.session_state.messages)
        full_response = st.write_stream(response_stream)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
    st.rerun()