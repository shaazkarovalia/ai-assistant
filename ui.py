import streamlit as st

def apply_custom_styling():
    st.markdown("""
    <style>
        /* Force Light Mode & Setup */
        .stApp { background-color: white !important; color: #333 !important; }
        .block-container { padding-top: 2rem; padding-bottom: 5rem; max-width: 800px; }

        /* --- HEADER --- */
        .header-top {
            font-size: clamp(2rem, 8vw, 3rem); 
            font-weight: 800; margin-bottom: -10px;
            background: linear-gradient(90deg, #6a11cb 0%, #8f43c1 100%);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }
        .header-bottom {
             font-size: clamp(2rem, 8vw, 3rem);
             font-weight: 800; margin-bottom: 20px; color: #ec4899; 
        }
        .emoji-fix { -webkit-text-fill-color: initial !important; background: none !important; }
        .sub-header { font-size: 1rem; color: #666 !important; margin-bottom: 30px; line-height: 1.4; }

        /* --- THE FLEX GRID (Always 4 in a Row) --- */
        .custom-card-row {
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: nowrap !important; /* Stack hone se roko */
            gap: 6px !important;
            width: 100% !important;
            justify-content: space-between;
            margin-bottom: 20px;
        }

        .card-box {
            flex: 1; 
            background: #ffffff;
            border: 1px solid #e0e0e0;
            border-radius: 12px;
            padding: 10px;
            height: 180px; /* Lamba text fit karne ke liye height badhayi */
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            min-width: 0;
        }

        .card-icon { font-size: 1.2rem; margin-bottom: 5px; }
        
        .card-text { 
            /* Mobile par text ko tiny kar dega taaki lamba sentence row na tode */
            font-size: clamp(0.55rem, 1.8vw, 0.85rem); 
            font-weight: 500; color: #333 !important;
            line-height: 1.2;
            word-wrap: break-word;
        }

        /* --- HIDDEN BUTTON HACK --- */
        .button-overlay-container {
            display: flex;
            flex-direction: row;
            gap: 6px;
            margin-top: -200px; /* Height ke hisab se adjust kiya */
            height: 180px;
        }
        
        .button-overlay-container div[data-testid="column"] {
            flex: 1 !important;
            min-width: 0 !important;
        }

        div.stButton > button {
            width: 100% !important;
            height: 180px !important;
            background: transparent !important;
            border: none !important;
            color: transparent !important;
            cursor: pointer;
        }

        #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

def show_landing_page():
    # 1. Header
    st.markdown(f"""
        <div class='header-top'>Hey User <span class='emoji-fix'>👋</span></div>
        <div class='header-bottom'>What can I help you with?</div>
        <p class='sub-header'>Handcrafted by <b>Shaaz Ali</b>. From zero to hero, let's build something amazing together! 🚀<br>
        <span style='font-size: 0.8rem; opacity: 0.8;'>Premium, top-shelf prompts. Use them wisely! 😉</span></p>
    """, unsafe_allow_html=True)

    # Original Long Prompts List
    prompts = [
        "Create a step-by-step plan for launching a new product",
        "Write a polite email to decline an invitation to a Webinar",
        "Summarize this blog post in a few key points",
        "Explain blockchain in simple terms, assume I am a 5 YO"
    ]

    # 2. Visual HTML Cards (Same UI, but with Full Long Prompts)
    st.markdown(f"""
        <div class="custom-card-row">
            <div class="card-box">
                <div class="card-icon">🚀</div>
                <div class="card-text">{prompts[0]}</div>
            </div>
            <div class="card-box">
                <div class="card-icon">📩</div>
                <div class="card-text">{prompts[1]}</div>
            </div>
            <div class="card-box">
                <div class="card-icon">📝</div>
                <div class="card-text">{prompts[2]}</div>
            </div>
            <div class="card-box">
                <div class="card-icon">🧠</div>
                <div class="card-text">{prompts[3]}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 3. Functional Buttons (Invisible Overlay)
    cols = st.columns(4)
    st.markdown("<div class='button-overlay-container'>", unsafe_allow_html=True)
    for i, col in enumerate(cols):
        with col:
            if st.button(" ", key=f"btn_{i}"):
                st.session_state.prompt_clicked = prompts[i]
    st.markdown("</div>", unsafe_allow_html=True)