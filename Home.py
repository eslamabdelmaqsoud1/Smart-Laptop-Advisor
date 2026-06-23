import streamlit as st

st.set_page_config(
    page_title="Smart Laptop Advisor",
    page_icon="💻",
    layout="wide"
)

# ==========================
# Button Style
# ==========================

st.markdown("""
<style>

.stButton > button {
    width:100%;
    height:70px;
    font-size:22px;
    font-weight:bold;
    border-radius:15px;
    border:none;
    background:#2563EB;
    color:white;
}

.stButton > button:hover {
    background:#1D4ED8;
    transition:0.3s;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# Header
# ==========================

st.title("💻 Smart Laptop Advisor")

st.markdown("""
### AI-Powered Laptop Selection System

This system helps users:

- 💰 Predict laptop prices using Machine Learning
- 🎯 Get laptop recommendations based on their needs
- ⚡ Compare different laptop categories

---
""")

# ==========================
# Services
# ==========================

st.subheader("Choose a Service")

col1, col2 = st.columns(2)

with col1:

    st.write("Predict laptop prices based on specifications.")

    if st.button(
        "💰 Price Prediction",
        use_container_width=True,
        key="price_btn"
    ):
        st.switch_page("pages/Price_Prediction.py")

with col2:

    st.write("Get the best laptop according to budget and usage.")

    if st.button(
        "🎯 Recommendation System",
        use_container_width=True,
        key="rec_btn"
    ):
        st.switch_page("pages/Recommendation_System.py")

st.markdown("---")

st.caption(
    "Graduation Project - Faculty of Computers and Artificial Intelligence"
)