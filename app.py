import streamlit as st
import ui 
import logic 

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Shaaz's AI Assistant",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. SETUP & STATE ---
ui.apply_custom_styling()
client = logic.initialize_groq_client()

if "messages" not in st.session_state:
    st.session_state.messages = []
if "prompt_clicked" not in st.session_state:
    st.session_state.prompt_clicked = None

# --- 3. HELPER FUNCTION ---
def process_chat(user_input):
    # User Message add karo
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Ye block chat dikhayega (history + current)
    # Note: Hum history neeche loop me dikhayenge, yahan sirf response generate ho raha hai

# --- 4. MAIN FLOW ---

# AGAR HISTORY KHALI HAI -> Landing Page dikhao
if not st.session_state.messages:
    # Saari landing UI yahan wrap kar di hai
    ui.show_header()
    ui.show_prompt_cards()
    # Koi extra st.write("<br>") bahar mat rakhna
else:
    # Agar history hai, toh landing UI skip ho jayegi aur chat top se shuru hogi
    pass

# --- 5. CHAT HISTORY DISPLAY ---
# Ye history hamesha render hogi. Agar landing page upar nahi hai, toh ye top par aa jayegi
for message in st.session_state.messages:
    avatar = "🧑‍💻" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# --- 6. INPUT HANDLING & RESPONSE ---
user_input = st.chat_input("Message Chat...")

# Prompt Card Click Logic
if st.session_state.prompt_clicked:
    current_prompt = st.session_state.prompt_clicked
    st.session_state.prompt_clicked = None # Reset
    st.session_state.messages.append({"role": "user", "content": current_prompt})
    st.rerun() # Refresh taaki landing page gayab ho jaye aur chat start ho

# Manual Input Logic
elif user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Response generation (Streaming)
    with st.chat_message("assistant", avatar="🤖"):
        response_stream = logic.get_ai_response_stream(client, st.session_state.messages)
        full_response = st.write_stream(response_stream)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
    st.rerun() # Final refresh logic ko clean rakhne ke liye