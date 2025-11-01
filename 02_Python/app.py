import streamlit as st
import pickle
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Game Category Predictor",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load the saved model
with open("game_model.pkl", "rb") as f:
    model = pickle.load(f)

# Professional CSS styling
st.markdown("""
    <style>
    /* Import professional font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Modern dark theme */
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #2d1b4e 100%);
        color: #e8eaed;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Professional header */
    .main-header {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(168, 85, 247, 0.1) 100%);
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 40px;
        border: 1px solid rgba(99, 102, 241, 0.2);
        box-shadow: 0 8px 32px rgba(99, 102, 241, 0.1);
    }
    
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 10px;
    }
    
    .subtitle {
        font-size: 1.1rem;
        color: #9ca3af;
        font-weight: 300;
        letter-spacing: 1px;
    }
    
    /* Form container */
    .form-container {
        background: rgba(255, 255, 255, 0.03);
        padding: 40px;
        border-radius: 20px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }
    
    .section-header {
        font-size: 1.3rem;
        font-weight: 600;
        color: #a855f7;
        margin-bottom: 25px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    /* Input styling */
    .stSelectbox, .stTextInput {
        margin-bottom: 20px;
    }
    
    .stSelectbox > label, .stTextInput > label {
        color: #d1d5db !important;
        font-weight: 500 !important;
        font-size: 0.95rem !important;
        margin-bottom: 8px !important;
    }
    
    .stSelectbox > div > div, .stTextInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(99, 102, 241, 0.3) !important;
        border-radius: 12px !important;
        color: #e8eaed !important;
        padding: 12px !important;
        transition: all 0.3s ease !important;
    }
    
    .stSelectbox > div > div:hover, .stTextInput > div > div > input:hover {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1) !important;
    }
    
    .stSelectbox > div > div:focus-within, .stTextInput > div > div > input:focus {
        border-color: #a855f7 !important;
        box-shadow: 0 0 0 3px rgba(168, 85, 247, 0.2) !important;
    }
    
    /* Professional button */
    .stButton {
        display: flex;
        justify-content: center;
        margin-top: 30px;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        font-weight: 600;
        font-size: 1.1rem;
        border: none;
        border-radius: 12px;
        padding: 18px 60px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(99, 102, 241, 0.3);
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 40px rgba(99, 102, 241, 0.4);
        background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Success message */
    .success-box {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(5, 150, 105, 0.1) 100%);
        border: 2px solid #10b981;
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        margin-top: 30px;
        animation: slideDown 0.5s ease-out;
    }
    
    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .success-box h3 {
        color: #10b981;
        font-size: 1.5rem;
        margin-bottom: 10px;
    }
    
    .success-box p {
        font-size: 2rem;
        font-weight: 700;
        color: #fff;
        margin: 0;
    }
    
    /* Stats cards */
    .stats-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(99, 102, 241, 0.2);
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .stats-card:hover {
        transform: translateY(-5px);
        border-color: #6366f1;
        box-shadow: 0 10px 30px rgba(99, 102, 241, 0.2);
    }
    
    .stats-number {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .stats-label {
        color: #9ca3af;
        font-size: 0.9rem;
        margin-top: 5px;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 40px;
        margin-top: 60px;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .footer-text {
        color: #9ca3af;
        font-size: 0.95rem;
    }
    
    .footer-brand {
        color: #a855f7;
        font-weight: 600;
    }
    
    /* Divider */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(99, 102, 241, 0.3), transparent);
        margin: 40px 0;
    }
    
    /* Info box */
    .info-box {
        background: rgba(59, 130, 246, 0.1);
        border-left: 4px solid #3b82f6;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        color: #bfdbfe;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="main-header">
        <div class="main-title">🎮 Game Category Predictor</div>
        <div class="subtitle">AI-Powered Game Classification System</div>
    </div>
""", unsafe_allow_html=True)

# Stats overview
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
        <div class="stats-card">
            <div class="stats-number">95%</div>
            <div class="stats-label">Accuracy</div>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div class="stats-card">
            <div class="stats-number">8</div>
            <div class="stats-label">Features</div>
        </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
        <div class="stats-card">
            <div class="stats-number">10K+</div>
            <div class="stats-label">Games Analyzed</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Information box
st.markdown("""
    <div class="info-box">
        <strong>ℹ️ How it works:</strong> Enter the game specifications below, and our machine learning model will predict the most suitable category for your game based on historical data and patterns.
    </div>
""", unsafe_allow_html=True)

# Main form
st.markdown('<div class="form-container">', unsafe_allow_html=True)

# Game Information Section
st.markdown('<div class="section-header">📊 Game Information</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    name_categorized = st.text_input("Game Title", placeholder="Enter game name...")
    target_audience = st.selectbox(
        "Target Audience",
        ["Teens", "Adults", "Teens/Adults"],
        help="Select the primary target audience for this game"
    )
    age_range = st.selectbox(
        "Age Range",
        ["13-19", "13-25", "20-40"],
        help="Recommended age range for players"
    )
    skills = st.selectbox(
        "Skill Level Required",
        ["Low", "Medium", "High"],
        help="Complexity and skill level needed to play"
    )

with col2:
    multiplayer = st.selectbox(
        "Multiplayer Support",
        ["Yes", "No"],
        help="Does the game support multiplayer mode?"
    )
    platform = st.selectbox(
        "Gaming Platform",
        ["PS2", "PS3", "X360", "XOne", "DS", "PS"],
        help="Primary gaming platform"
    )
    publisher = st.selectbox(
        "Publisher",
        ["Electronic Arts", "Ubisoft", "Konami", "Warner Bros.", "Other"],
        help="Game publisher or distributor"
    )
    publisher_category = st.selectbox(
        "Publisher Category",
        ["EA", "Ubisoft", "Konami", "Warner Bros", "Other"],
        help="Publisher classification"
    )

# Collect inputs into a dataframe
input_df = pd.DataFrame({
    "Target_Audience": [target_audience],
    "Age_Range": [age_range],
    "Skills": [skills],
    "Multiplayer": [multiplayer],
    "Publisher": [publisher],
    "Name_Categorized": [name_categorized],
    "Publisher_Category": [publisher_category],
    "Platform": [platform]
})

# Predict button (centered)
col_left, col_center, col_right = st.columns([1.73, 2, 1])
with col_center:
    if st.button("🚀 Predict Category"):
        if name_categorized:
            with st.spinner("🔄 Analyzing game data..."):
                pred = model.predict(input_df)
                st.markdown(f"""
                    <div class="success-box">
                        <h3>✅ Prediction Complete</h3>
                        <p>{pred[0]}</p>
                    </div>
                """, unsafe_allow_html=True)
                st.balloons()
        else:
            st.error("⚠️ Please enter a game name to proceed with prediction.")

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <div class="footer-text">
            | Developed by <span class="footer-brand">Ahmed Ameen</span> | 
        </div>
        <div style="margin-top: 10px; color: #6b7280; font-size: 0.85rem;">
            © 2025 Game Category Predictor. All rights reserved.
        </div>
    </div>
""", unsafe_allow_html=True)
