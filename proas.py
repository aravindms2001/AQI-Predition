import streamlit as st
import pickle
st.markdown("""
    <style>
    body {
        background-color: #f0f8ff;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Air Quality Index Predictor")

# st.markdown("""
#     <h3 style='text-decoration: underline; color: #2e8b57;'>About the Project</h3>
#     <div style='background-color: #f9f9f9; border: 1px solid #ddd; padding: 20px; border-radius: 10px; font-size: 16px; line-height: 1.6; color: #333;'>
#     <strong>Breathing Easy with Data-Driven Insights</strong><br><br>
#     Air pollution is a growing concern worldwide, impacting human health and ecosystems. Our project leverages Machine Learning to predict Air Quality Index (AQI) values, empowering individuals and governments to make informed decisions.<br><br>
#     <strong>Our Approach</strong><br>
#     - Utilize historical air quality data from Kerala, India<br>
#     - Train a Random Forest regression model on pollutant concentrations (PM2.5, PM10, CO, NO, NO₂, NOx, SO₂, NH₃, O₃)<br>
#     - Predict AQI values and visualize trends for better environmental management and public awareness<br><br>
#     <strong>Our Goal</strong><br>
#     To provide accurate AQI predictions, enabling proactive measures to mitigate air pollution's adverse effects and promote a healthier environment.
#     </div>
#     """, unsafe_allow_html=True)
            


st.subheader("Enter Pollutant Concentrations:")
CO = st.number_input("Carbon Monoxide (CO)")
Ozone = st.number_input("Ozone (O₃)")
NO = st.number_input("Nitric Oxide (NO)")
NO2 = st.number_input("Nitrogen Dioxide (NO₂)")
NOX = st.number_input("Nitrogen Oxides (NOx)")
NH3 = st.number_input("Ammonia (NH₃)")
SO2 = st.number_input("Sulphur Dioxide (SO₂)")
PM25 = st.number_input("Particulate Matter ≤ 2.5 μm (PM2.5)")
PM10 = st.number_input("Particulate Matter ≤ 10 μm (PM10)")

if st.button("Predict"):

        file=open(r"C:\Users\sonusnair\Downloads\li.pkl")
        classifier = pickle.load(file``)
        prediction = classifier.predict([[CO, Ozone, NO, NO2, NOX, NH3, SO2, PM25, PM10]])
        predicted_aqi = prediction


        if predicted_aqi <= 50:
            st.success("Good ✅")
        elif predicted_aqi <= 100:
            st.info("Moderate 🌤️")
        elif predicted_aqi <= 150:
            st.warning("Unhealthy for Sensitive Groups ⚠️")
        elif predicted_aqi <= 200:
            st.error("Unhealthy 🛑")
        elif predicted_aqi <= 300:
            st.error("Very Unhealthy ☣️")
        elif predicted_aqi <= 500:
            st.error("Hazardous ☠️")
        else:
            st.write("No data 💼")
         
st.markdown("🧠 Built with Machine Learning · 🌏 For cleaner air in Kerala!")