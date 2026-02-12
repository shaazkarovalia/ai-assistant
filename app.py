import streamlit as st
import ui  
import logic 

# --- 1. CONFIGURATION (Must be first) ---
st.set_page_config(
    page_title="Shaaz's AI Assistant",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. SETUP ---
ui.apply_custom_styling()  # UI file se CSS lagayi
client = logic.initialize_groq_client() # Logic file se client liya

# Session State Init
if "messages" not in st.session_state:
    st.session_state.messages = []
if "prompt_clicked" not in st.session_state:
    st.session_state.prompt_clicked = None

# --- 3. HELPER FUNCTION TO PROCESS CHAT ---
def process_chat(user_input):
    # 1. User Message Display
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(user_input)

    # 2. Assistant Response Display
    with st.chat_message("assistant", avatar="🤖"):
        # Logic file se stream function call kiya
        response_stream = logic.get_ai_response_stream(client, st.session_state.messages)
        # Streamlit ka magic function jo stream ko print karta hai
        full_response = st.write_stream(response_stream)
        
        # History update
        st.session_state.messages.append({"role": "assistant", "content": full_response})

# --- 4. MAIN APP FLOW ---

# Agar chat history khali hai, toh Header aur Cards dikhao
if not st.session_state.messages:
    ui.show_header()
    st.write("") 
    ui.show_prompt_cards()
    st.write("<br>", unsafe_allow_html=True) 

# Purani History Display karo
for message in st.session_state.messages:
    avatar = "🧑‍💻" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# --- 5. INPUT HANDLING ---
user_input = st.chat_input("Message Chat...")

if st.session_state.prompt_clicked:
    process_chat(st.session_state.prompt_clicked)
    st.session_state.prompt_clicked = None
    st.rerun()
elif user_input:
    process_chat(user_input)