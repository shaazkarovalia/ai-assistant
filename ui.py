import streamlit as st

def apply_custom_styling():
    st.markdown("""
    <style>
        /* --- GLOBAL LIGHT MODE FORCE --- */
        .stApp { background-color: white !important; color: #333 !important; }
        .block-container { padding-top: 2rem; padding-bottom: 5rem; }
        
        /* --- HEADER STYLES --- */
        .header-top {
            font-size: 3rem; font-weight: 800; margin-bottom: -15px;
            background: linear-gradient(90deg, #6a11cb 0%, #8f43c1 100%);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }
        .header-bottom { font-size: 3rem; font-weight: 800; margin-bottom: 20px; color: #ec4899; }
        .emoji-fix { -webkit-text-fill-color: initial !important; background: none !important; }
        .sub-header { font-size: 1.1rem; color: #666 !important; margin-bottom: 40px; }

        /* --- STANDARD CARD STYLES (Laptop) --- */
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
        .card-icon { font-size: 1.5rem; margin-bottom: 10px; color: #2575fc; }
        .card-text { font-size: 0.9rem; font-weight: 500; color: #333 !important; }
        .card-wrapper { margin-top: -195px; }
        div.stButton > button:first-child { height: 180px; }


        /* =========================================
           MOBILE AGGRESSIVE OVERRIDE (The Magic Fix)
        ========================================= */
        @media (max-width: 768px) {
            
            /* 1. Force Streamlit Columns to stay in a ROW */
            /* Hum Streamlit ke internal container ko pakad ke bol rahe hain: Stack mat hona! */
            div[data-testid="column"] {
                flex: 1 1 auto !important; /* Sab barabar space lein */
                width: auto !important;
                min-width: 70px !important; /* Isse chota nahi hoga, warna fat jayega */
            }
            
            /* Columns ke beech ka gap kam karo */
            div[data-testid="stHorizontalBlock"] {
                gap: 0.5rem !important;
            }

            /* 2. Shrink Card Size & Content */
            .prompt-card {
                height: 130px !important; /* Height kam ki */
                padding: 10px !important; /* Padding kam ki */
                border-radius: 10px !important;
            }
            
            /* Icon chota karo */
            .card-icon {
                font-size: 1rem !important;
                margin-bottom: 5px !important;
            }
            
            /* Text bohot chota karo taaki fit aaye */
            .card-text {
                font-size: 0.65rem !important;
                line-height: 1.1 !important;
            }

            /* 3. Adjust Button Alignment Hack */
            div.stButton > button:first-child {
                height: 130px !important; /* Match new card height */
            }
            .card-wrapper {
                margin-top: -145px !important; /* Adjust overlap margin */
            }

            /* Header fonts bhi thode chote karo mobile pe */
            .header-top, .header-bottom { font-size: 1.8rem !important; }
        }

        /* Button invisibility hack */
        div.stButton > button:first-child {
            width: 100%; background-color: transparent !important;
            border: none !important; color: transparent !important;
            position: relative; z-index: 2;
        }
        #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

def show_header():
    st.markdown("<div class='header-top'>Hey User <span class='emoji-fix'>👋</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='header-bottom'>What can I help you with?</div>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Handcrafted by <b>Shaaz Ali</b>. From zero to hero, let's build something amazing together! 🚀</p>", unsafe_allow_html=True)

def show_prompt_cards():
    col1, col2, col3, col4 = st.columns(4)
    prompts = [
        {"icon": "🚀", "text": "Create a step-by-step plan for product launch"}, # Text thoda chota kiya mobile ke liye
        {"icon": "📩", "text": "Write a polite decline email for a webinar"},
        {"icon": "📝", "text": "Summarize this blog post in key points"},
        {"icon": "🧠", "text": "Explain blockchain to a 5 year old"}
    ]

    def create_card(col, prompt_data):
        with col:
            st.markdown(f"""
            <div class="prompt-card">
                <div class="card-icon">{prompt_data['icon']}</div>
                <div class="card-text">{prompt_data['text']}</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<div class='card-wrapper'></div>", unsafe_allow_html=True) 
            if st.button(" " * 20, key=prompt_data['text']): 
                 st.session_state.prompt_clicked = prompt_data['text']

    create_card(col1, prompts[0])
    create_card(col2, prompts[1])
    create_card(col3, prompts[2])
    create_card(col4, prompts[3])