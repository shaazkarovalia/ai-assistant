import streamlit as st

def apply_custom_styling():
    st.markdown("""
    <style>
        /* Force Light Mode & Basic Setup */
        .stApp { background-color: white !important; color: #333 !important; }
        .block-container { padding-top: 2rem; padding-bottom: 5rem; max-width: 800px; }

        /* --- HEADER --- */
        .header-top {
            font-size: clamp(2rem, 8vw, 3rem); /* Responsive Font */
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

        /* --- THE FLEX GRID (The Magic Fix) --- */
        /* Humne Streamlit ke columns ki jagah apna container banaya hai */
        .custom-card-row {
            display: flex !important;
            flex-direction: row !important; /* Hamesha ek line mein */
            flex-wrap: nowrap !important; /* Stack hone se roko */
            gap: 8px !important;
            width: 100% !important;
            justify-content: space-between;
            margin-bottom: 20px;
        }

        .card-box {
            flex: 1; /* Sab barabar jagah lein */
            background: #ffffff;
            border: 1px solid #e0e0e0;
            border-radius: 12px;
            padding: 10px;
            height: 140px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            text-align: left;
            min-width: 0; /* Overflow rokne ke liye */
        }

        .card-icon { font-size: 1.2rem; margin-bottom: 5px; }
        .card-text { 
            font-size: clamp(0.6rem, 2vw, 0.85rem); /* Text screen ke hisab se chota hoga */
            font-weight: 500; color: #333 !important;
            line-height: 1.2;
            word-wrap: break-word;
        }

        /* --- HIDDEN BUTTON HACK --- */
        /* Visual cards ke neeche asli buttons ko invisible kar ke fit karna */
        .button-overlay-container {
            display: flex;
            flex-direction: row;
            gap: 8px;
            margin-top: -160px; /* Card ke upar le aao */
            height: 140px;
        }
        
        .button-overlay-container div[data-testid="column"] {
            flex: 1 !important;
            min-width: 0 !important;
        }

        div.stButton > button {
            width: 100% !important;
            height: 140px !important;
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

    # 2. Visual HTML Cards (Sirf dikhne ke liye)
    st.markdown("""
        <div class="custom-card-row">
            <div class="card-box">
                <div class="card-icon">🚀</div>
                <div class="card-text">Product launch plan</div>
            </div>
            <div class="card-box">
                <div class="card-icon">📩</div>
                <div class="card-text">Decline webinar email</div>
            </div>
            <div class="card-box">
                <div class="card-icon">📝</div>
                <div class="card-text">Blog summary points</div>
            </div>
            <div class="card-box">
                <div class="card-icon">🧠</div>
                <div class="card-text">Explain blockchain (5YO)</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 3. Functional Buttons (Click karne ke liye - Invisible)
    # Hum 4 columns banayenge jo exactly upar wale boxes ke size ke honge
    cols = st.columns(4)
    prompts = [
        "Create a step-by-step plan for launching a new product",
        "Write a polite email to decline an invitation to a Webinar",
        "Summarize this blog post in a few key points",
        "Explain blockchain in simple terms, assume I am a 5 YO"
    ]
    
    # Is container ko CSS ke zariye humne cards ke upar "overlay" kar diya hai
    st.markdown("<div class='button-overlay-container'>", unsafe_allow_html=True)
    for i, col in enumerate(cols):
        with col:
            if st.button(" ", key=f"btn_{i}"):
                st.session_state.prompt_clicked = prompts[i]
    st.markdown("</div>", unsafe_allow_html=True)