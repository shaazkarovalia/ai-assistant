import streamlit as st

def apply_custom_styling():
    st.markdown("""
    <style>
        /* --- 1. REMOVE STREAMLIT TOP SPACE --- */
        /* Isse wo invisible jagah khatam ho jayegi jo content ko neeche dhakelti hai */
        [data-testid="stHeader"] {
            display: none !important;
        }
        
        [data-testid="stDecoration"] {
            display: none !important;
        }

        /* --- 2. FORCE CONTENT TO TOP --- */
        .block-container { 
            padding-top: 0rem !important; /* Header ka gap bilkul khatam */
            padding-bottom: 0rem !important;
            max-width: 800px;
            margin-top: 0px !important;
        }

        /* --- 3. VIEWPORT LOCK --- */
        html, body, [data-testid="stAppViewContainer"] {
            height: 100vh;
            overflow: hidden !important;
            margin: 0;
            padding: 0;
        }

        [data-testid="stMainViewContainer"] {
            height: 100vh;
            overflow-y: auto !important;
            overflow-x: hidden !important;
            display: flex;
            flex-direction: column;
        }

        .stApp { background-color: white !important; color: #333 !important; }

        /* --- 4. HEADER STYLING --- */
        .header-top {
            font-size: clamp(1.5rem, 7vw, 3rem); 
            font-weight: 800; 
            margin-top: 10px; /* Thoda sa saans lene ki jagah */
            margin-bottom: -10px;
            background: linear-gradient(90deg, #6a11cb 0%, #8f43c1 100%);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }
        .header-bottom {
             font-size: clamp(1.5rem, 7vw, 3rem);
             font-weight: 800; margin-bottom: 10px; color: #ec4899; 
        }
        .emoji-fix { -webkit-text-fill-color: initial !important; background: none !important; }
        .sub-header { font-size: 0.9rem; color: #666 !important; margin-bottom: 20px; }

        /* --- 5. FLEX GRID (Responsive Row) --- */
        .custom-card-row {
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            gap: 5px !important;
            width: 100% !important;
            justify-content: space-between;
            margin-bottom: 15px;
        }

        .card-box {
            flex: 1; 
            background: #ffffff;
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            padding: 8px;
            height: 140px; 
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            min-width: 0;
        }

        .card-text { 
            font-size: clamp(0.55rem, 1.8vw, 0.8rem); 
            font-weight: 500; color: #333 !important;
            line-height: 1.1;
        }

        /* --- 6. OVERLAY FIX --- */
        .button-overlay-container {
            display: flex;
            flex-direction: row;
            gap: 5px;
            margin-top: -155px; /* Box height adjustment */
            height: 140px;
        }
        
        div.stButton > button {
            width: 100% !important;
            height: 140px !important;
            background: transparent !important;
            border: none !important;
            color: transparent !important;
        }

        #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

def show_landing_page():
    st.markdown(f"""
        <div class='header-top'>Hey User <span class='emoji-fix'>👋</span></div>
        <div class='header-bottom'>What can I help you with?</div>
        <p class='sub-header'>Handcrafted by <b>Shaaz Ali</b>. Build something amazing! 🚀</p>
    """, unsafe_allow_html=True)

    prompts = [
        "Create a step-by-step plan for launching a new product",
        "Write a polite email to decline an invitation to a Webinar",
        "Summarize this blog post in a few key points",
        "Explain blockchain in simple terms, assume I am a 5 YO"
    ]

    st.markdown(f"""
        <div class="custom-card-row">
            <div class="card-box"><div style="font-size: 1rem;">🚀</div><div class="card-text">{prompts[0]}</div></div>
            <div class="card-box"><div style="font-size: 1rem;">📩</div><div class="card-text">{prompts[1]}</div></div>
            <div class="card-box"><div style="font-size: 1rem;">📝</div><div class="card-text">{prompts[2]}</div></div>
            <div class="card-box"><div style="font-size: 1rem;">🧠</div><div class="card-text">{prompts[3]}</div></div>
        </div>
    """, unsafe_allow_html=True)

    cols = st.columns(4)
    st.markdown("<div class='button-overlay-container'>", unsafe_allow_html=True)
    for i, col in enumerate(cols):
        with col:
            if st.button(" ", key=f"btn_{i}"):
                st.session_state.prompt_clicked = prompts[i]
    st.markdown("</div>", unsafe_allow_html=True)