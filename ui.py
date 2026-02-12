import streamlit as st

def apply_custom_styling():
    st.markdown("""
    <style>
        /* Main Container Spacing */
        .block-container {
            padding-top: 3rem;
            padding-bottom: 5rem;
        }
        
        /* Header Styling */
        .header-top {
            font-size: 3rem;
            font-weight: 800;
            margin-bottom: -15px;
            background: linear-gradient(90deg, #6a11cb 0%, #8f43c1 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        /* Emoji Fix Class */
        .emoji-fix {
            -webkit-text-fill-color: initial !important; 
            background: none !important;
        }

        .header-bottom {
             font-size: 3rem;
             font-weight: 800;
             margin-bottom: 20px;
             color: #ec4899; 
        }
        
        .sub-header {
            font-size: 1.1rem;
            color: #666;
            margin-bottom: 40px;
            line-height: 1.5;
        }
        
        /* Prompt Card Styling */
        .prompt-card {
            background-color: #ffffff;
            border: 1px solid #e0e0e0;
            border-radius: 16px;
            padding: 20px;
            text-align: left;
            height: 180px; 
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
            pointer-events: none; 
        }
        
        div.stButton > button:first-child {
            width: 100%;
            height: 180px; 
            background-color: transparent;
            border: none;
            color: transparent;
            position: relative;
            z-index: 2; 
        }
        
        /* Sidebar Button Protection */
        section[data-testid="stSidebar"] div.stButton > button:first-child {
            height: auto !important;
            background-color: #FF4B4B !important; 
            color: white !important;
        }
        
        /* Hide Default Streamlit Elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

def show_header():
    st.markdown("<div class='header-top'>Hey User <span class='emoji-fix'>👋</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='header-bottom'>What can I help you with?</div>", unsafe_allow_html=True)
    
    st.markdown(
        "<p class='sub-header'>Handcrafted by <b>Shaaz Ali</b>. From zero to hero, let's build something amazing together! 🚀<br>"
        "<span style='font-size: 0.9rem; color: #888;'>Premium, top-shelf prompts. Use them wisely! 😉</span></p>", 
        unsafe_allow_html=True
    )

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
            card_html = f"""
            <div class="prompt-card">
                <div style="font-size: 1.5rem; margin-bottom: 10px; color: #2575fc;">{prompt_data['icon']}</div>
                <div style="font-size: 0.9rem; font-weight: 500; color: #333; line-height: 1.4;">{prompt_data['text']}</div>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
            st.markdown("<div style='margin-top: -195px;'></div>", unsafe_allow_html=True) 
            
            if st.button(" " * 10, key=prompt_data['text']): 
                 st.session_state.prompt_clicked = prompt_data['text']

    create_card(col1, prompts[0])
    create_card(col2, prompts[1])
    create_card(col3, prompts[2])
    create_card(col4, prompts[3])