import streamlit as st
st.set_page_config(page_title="Possum Age Predictor", layout="wide", page_icon="🦝")
from Possum_age_predictor import Predictor
# -------------------------------------------------
# ✅ MODERN UI STYLING
# -------------------------------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

/* 🧊 Main Card Glassmorphism */
.main {
    background: linear-gradient(
        135deg,
        rgba(255, 255, 255, 0.18),
        rgba(255, 255, 255, 0.08)
    );
    padding: 2.5rem;
    border-radius: 22px;
    box-shadow: 
        0px 0px 30px rgba(0, 0, 0, 0.4),
        inset 0px 0px 20px rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(12px);
}

/* 🔥 Main Heading */
h1 {
    text-align: center;
    font-size: 44px;
    font-weight: 800;
    background: linear-gradient(to right, #ff512f, #f09819, #00c6ff);
    -webkit-background-clip: text;
    color: transparent;
    text-shadow: 0px 0px 25px rgba(255, 120, 0, 0.25);
}

/* ✨ Subheading */
h3 {
    text-align: center;
    font-size: 22px;
    color: #00ffd5;
    text-shadow: 0px 0px 12px rgba(0, 255, 213, 0.5);
}

/* 🏷️ Labels */
label {
    color: #ffffff !important;
    font-weight: 700;
    font-size: 15px;
    text-shadow: 0px 0px 6px rgba(255,255,255,0.3);
}

/* ✅ Button Styling */
.stButton > button {
    width: 60%;
    background: linear-gradient(90deg, #11998e, #38ef7d);
    color: black;
    font-size: 20px;
    border-radius: 12px;
    padding: 10px;
    border: none;
    transition: 0.3s;
    display: block;
    margin: auto;
}

.stButton > button:hover {
    transform: scale(1.08);
}

/* ✅ Prediction Box */
.pred-box {
    text-align: center;
    font-size: 30px;
    font-weight: bold;
    padding: 25px;
    border-radius: 15px;
    background: linear-gradient(135deg, #f7971e, #ffd200);
    color: black;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)


# -------------------------------------------------
# ✅ HEADER
# -------------------------------------------------
st.markdown("""
<div style="background-color:#ffcc00;padding:15px;border-radius:10px;">
    <h2 style="color:black;text-align:center;">🦝 Possum Age Predictor</h2>
</div>
""", unsafe_allow_html=True)
st.divider()

# -------------------------------------------------
# ✅ INPUT SECTION — EXACT FEATURES
# -------------------------------------------------
st.subheader("🔢 Enter Possum Measurements")

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    hdlngth = st.number_input("Head Length (hdlngth)", step=0.1)
with c2:
    sex = st.selectbox("Sex", ["m", "f"])   # string
with c3:
    skullw = st.number_input("Skull Width (skullw)", step=0.1)
with c4:
    totlngth = st.number_input("Total Length (totlngth)", step=0.1)
with c5:
    taill = st.number_input("Tail Length (taill)", step=0.1)

c6, c7, c8, c9, c10, c11 = st.columns(6)

with c6:
    footlgth = st.number_input("Foot Length (footlgth)", step=0.1)
with c7:
    earconch = st.number_input("Ear Conch (earconch)", step=0.1)
with c8:
    eye = st.number_input("Eye Width (eye)", step=0.1)
with c9:
    chest = st.number_input("Chest Girth (chest)", step=0.1)
with c10:
    belly = st.number_input("Belly Girth (belly)", step=0.1)
with c11:
    Pop = st.selectbox("Population (Pop)", ["Vic", "other"])  # string


# -------------------------------------------------
# ✅ ✅ CONVERT USER INPUT → EXACT DATAFRAME SCHEMA
# -------------------------------------------------
input_df = [hdlngth , sex , skullw , totlngth , taill , footlgth ,earconch , eye , chest , belly, Pop]

# -------------------------------------------------
# ✅ SHOW INPUT AS DATAFRAME (DEBUG + VISUAL)
# -------------------------------------------------
st.subheader("📊 Model Input (Exact DataFrame Schema)")
st.dataframe(input_df)

# -------------------------------------------------
# ✅ PREDICTION
# -------------------------------------------------
if st.button("🚀 Predict Possum Age"):
    predicted_age = Predictor(input_df)

    st.markdown(f"""
    <div class="pred-box">
        ✅ Predicted Possum Age <br>
        {predicted_age} Years
    </div>
    """, unsafe_allow_html=True)