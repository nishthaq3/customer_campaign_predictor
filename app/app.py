import streamlit as st
import pandas as pd
import os
import joblib

#Load model (robust path)
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "..", "model", "campaign_response_model.pkl")
model = joblib.load(model_path)


st.set_page_config(
    page_title="🛍️ Customer Campaign Response Predictor",
    page_icon="",
    layout="centered",
    initial_sidebar_state="expanded"
)

#CSS Styling

st.markdown(
    """
    <style>

    /* App background */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(to bottom right, #e6f2ff, #cce6ff) !important;
    }

    /* Title */
    h1 {
        color: #004080 !important;
        font-family: 'Arial', sans-serif;
        font-weight: 900;
        text-align: center;
    }

    /* About box */
    .about-text {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        border-left: 6px solid #3399ff;
        font-size: 16px;
        font-weight: 700;
        color: #003366;
        margin-bottom: 25px;
    }

    /* FORCE labels + subheaders to DARK NAVY */
    label,
    .stNumberInput label,
    .stSelectbox label,
    .stTextInput label,
    .css-1x8cf1d,
    .css-1kyxreq,
    .css-1emrehy,
    .css-1v0mbdj,
    h2, h3 {
        color: #00264d !important;
        font-weight: 900 !important;
    }

    /* Input box styling */
    div[role="spinbutton"] input,
    .stNumberInput input,
    .stTextInput input,
    .stSelectbox div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #00264d !important;
        border-radius: 8px;
        border: 1px solid #66a3ff !important;
    }

    /* Button styling */
    .stButton>button {
        background-color: #3399ff !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 0.6rem 1rem !important;
        font-size: 1.05rem !important;
        font-weight: 800 !important;
    }
    .stButton>button:hover {
        background-color: #1a8cff !important;
        transform: scale(1.03);
    }

    /* Result box */
    .result-box {
        background-color: #e6f2ff;
        padding: 20px;
        border-radius: 12px;
        border-left: 8px solid #3399ff;
        margin-top: 20px;
        font-size: 18px;
        font-weight: 800;
        color: #003366;
    }

    /* SIDEBAR heading fix */
    [data-testid="stSidebar"] h2 {
        color: white !important; 
        font-weight: 900 !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("## 📌 Navigation")  

menu = st.sidebar.selectbox(
    "Choose a section:",
    ["Overview", "Know the Model", "Contact Me"]
)

if menu == "Overview":
    st.sidebar.write(
        "**This tool predicts whether a customer will respond to a marketing campaign using ML.**"
    )

elif menu == "Know the Model":
    st.sidebar.write(
        "**This app uses a Support Vector Machine (SVM) classifier trained on customer behavior and demographics.**"
    )

elif menu == "Contact Me":
    st.sidebar.write("**Email:** nishthatripathi05@gmail.com\n\n**GitHub:** github.com/nishthaq3")

st.markdown("<h1>Customer Campaign Response Predictor🛍️</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="about-text">
    <strong>Welcome!</strong><br>
    This application uses <strong>machine learning</strong> to predict whether a customer is likely to <strong>respond positively</strong> to a marketing campaign.
    </div>
    """,
    unsafe_allow_html=True
)

#Input fields
st.markdown("### <strong>Enter Customer Details</strong>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    income = st.number_input("Income", min_value=0, key="income")
    kidhome = st.number_input("Kids at Home", min_value=0, max_value=5, key="kidhome")
    teenhome = st.number_input("Teenagers at Home", min_value=0, max_value=5, key="teenhome")
    recency = st.number_input("Recency (Days Since Last Purchase)", min_value=0, key="recency")
    education = st.selectbox("Education Level",
                             ["Graduation", "PhD", "Master", "Basic", "2n Cycle"],
                             key="education")
    marital = st.selectbox("Marital Status",
                           ["Married", "Single", "Divorced", "Together", "Widow", "Alone"],
                           key="marital")

with col2:
    num_deals = st.number_input("Number of Deal Purchases", min_value=0, key="deals")
    num_web = st.number_input("Number of Web Purchases", min_value=0, key="web")
    num_catalog = st.number_input("Number of Catalog Purchases", min_value=0, key="catalog")
    num_store = st.number_input("Number of Store Purchases", min_value=0, key="store")
    num_visits = st.number_input("Web Visits per Month", min_value=0, key="visits")
    complain = st.selectbox("Has Complained in Last 2 Years?", 
                            [0, 1],
                            key="complain")

input_df = pd.DataFrame({
    "Year_Birth": [1980],
    "Education": [education],
    "Marital_Status": [marital],
    "Income": [income],
    "Kidhome": [kidhome],
    "Teenhome": [teenhome],
    "Recency": [recency],
    "NumDealsPurchases": [num_deals],
    "NumWebPurchases": [num_web],
    "NumCatalogPurchases": [num_catalog],
    "NumStorePurchases": [num_store],
    "NumWebVisitsMonth": [num_visits],
    "Complain": [complain]
})


#Prediction
if st.button("Predict Customer Response"):
    result = model.predict(input_df)[0]
    if result == 1:
        st.markdown("<div class='result-box'><strong>This customer is LIKELY to respond to the marketing campaign!</strong></div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='result-box'><strong>This customer is NOT likely to respond to the marketing campaign.</strong></div>", unsafe_allow_html=True)
