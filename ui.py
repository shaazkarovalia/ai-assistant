import streamlit as st

def apply_custom_styling():
    st.markdown("""
    <style>
        /* Force Light Mode Styles */
        .stApp { background-color: white !important; color: #333 !important; }
        
        .block-container { padding-top: 2rem; padding-bottom: 5rem; }
        
        .header-top {
            font-size: 3rem; font-weight: 800; margin-bottom: -15px;
            background: linear-gradient(90deg, #6a11cb 0%, #8f43c1 100%);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }
        .header-bottom { font-size: 3rem; font-weight: 800; margin-bottom: 20px; color: #ec4899; }
        .emoji-fix { -webkit-text-fill-color: initial !important; background: none !important; }
        .sub-header { font-size: 1.1rem; color: #666 !important; margin-bottom: 40px; }

        /* --- RESPONSIVE CARD LOGIC --- */
        .prompt-card {
            background-color: #ffffff !important;
            border: 1px solid #e0e0e0;
            border-radius: 16px;
            padding: 20px;
            height: 180px; 
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        }

        /* Desktop View (Standard Alignment) */
        @media (min-width: 768px) {
            .card-wrapper { margin-top: -195px; }
            div.stButton > button:first-child { height: 180px; }
        }

        /* Mobile View (No Negative Margin) */
        @media (max-width: 767px) {
            .header-top, .header-bottom { font-size: 2rem !important; }
            .card-wrapper { margin-top: 0px !important; }
            div.stButton > button:first-child { 
                height: 180px !important; 
                margin-bottom: 10px;
            }
            .prompt-card { margin-bottom: 10px; }
        }

        /* Button invisibility hack */
        div.stButton > button:first-child {
            width: 100%; background-color: transparent !important;
            border: none !important; color: transparent !important;
            position: relative; z-index: 2;
        }
    </style>
    """, unsafe_allow_html=True)

def show_header():
    st.markdown("<div class='header-top'>Hey User <span class='emoji-fix'>👋</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='header-bottom'>What can I help you with?</div>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Handcrafted by <b>Shaaz Ali</b>. From zero to hero, let's build something amazing together! 🚀</p>", unsafe_allow_html=True)

def show_prompt_cards():
    col1, col2, col3, col4 = st.columns(4)
    prompts = [
        {"icon": "🚀", "text": "Create a step-by-step plan for launching a new product"},
        {"icon": "📩", "text": "Write a polite email to decline an invitation to a Webinar"},
        {"icon": "📝", "text": "Summarize this blog post in a few key points"},
        {"icon": "🧠", "text": "Explain blockchain in simple terms, assume I am a 5 YO"}
    ]

    def create_card(col, prompt_data):
        with col:
            st.markdown(f"""
            <div class="prompt-card">
                <div style="font-size: 1.5rem; margin-bottom: 10px; color: #2575fc;">{prompt_data['icon']}</div>
                <div style="font-size: 0.9rem; font-weight: 500; color: #333 !important;">{prompt_data['text']}</div>
            </div>
            """, unsafe_allow_html=True)
            # Wrapper class mobile logic handle karne ke liye
            st.markdown("<div class='card-wrapper'></div>", unsafe_allow_html=True) 
            if st.button(" " * 20, key=prompt_data['text']): 
                 st.session_state.prompt_clicked = prompt_data['text']

    create_card(col1, prompts[0])
    create_card(col2, prompts[1])
    create_card(col3, prompts[2])
    create_card(col4, prompts[3])