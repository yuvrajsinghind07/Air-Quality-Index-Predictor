import streamlit as st
import pandas as pd
import joblib

# Load Saved Pipeline
model = joblib.load("aqi_prediction_pipeline.pkl")

# Title
st.title("Air Quality Index Prediction")

st.write("Enter the pollutant values below to predict AQI.")

# Input Fields

city = st.selectbox(
    "Select City",
    ["Ahmedabad", "Bengaluru", "Chennai", "Delhi", "Hyderabad", "Kolkata", "Mumbai","Lucknow","Patna","Gurugram",
    "Visakhapatnam","Amritsar","Jaipur","Thiruvananthapuram","Chandigarh","Amaravati","Jorapokhar","Guwahati","Bhopal","Brajrajnagar",
    "Talcher","Coimbatore","Shillong","Kochi","Ernakulam","Aizawl"]
)

pm25 = st.number_input("PM2.5")
pm10 = st.number_input("PM10")
no = st.number_input("NO")
no2 = st.number_input("NO2")
nox = st.number_input("NOx")
nh3 = st.number_input("NH3")
co = st.number_input("CO")
so2 = st.number_input("SO2")
o3 = st.number_input("O3")
benzene = st.number_input("Benzene")
toluene = st.number_input("Toluene")
xylene = st.number_input("Xylene")

# Prediction

if st.button("Predict AQI"):

    input_data = pd.DataFrame({
        "City": [city],
        "PM2.5": [pm25],
        "PM10": [pm10],
        "NO": [no],
        "NO2": [no2],
        "NOx": [nox],
        "NH3": [nh3],
        "CO": [co],
        "SO2": [so2],
        "O3": [o3],
        "Benzene": [benzene],
        "Toluene": [toluene],
        "Xylene": [xylene]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted AQI : {prediction[0]:.2f}")

    # AQI Category

    if prediction[0] <= 50:
        st.success("AQI Category : Good")

    elif prediction[0] <= 100:
        st.success("AQI Category : Satisfactory")

    elif prediction[0] <= 200:
        st.warning("AQI Category : Moderate")

    elif prediction[0] <= 300:
        st.warning("AQI Category : Poor")

    elif prediction[0] <= 400:
        st.error("AQI Category : Very Poor")

    else:
        st.error("AQI Category : Severe")