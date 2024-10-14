import streamlit as st
from google.cloud import aiplatform

# กำหนดการตั้งค่า Google Cloud
aiplatform.init(project='YOUR_PROJECT_ID', location='YOUR_LOCATION')

def generate_response(prompt):
    # เรียกใช้ Google Generative AI API
    response = aiplatform.gapic.PredictionServiceClient().predict(
        endpoint='YOUR_ENDPOINT_ID',
        instances=[{"content": prompt}]
    )
    return response.predictions[0]['content']

st.title("AI Chatbot")

user_input = st.text_input("คุณ: ", "")

if st.button("ส่ง"):
    if user_input:
        response = generate_response(user_input)
        st.text_area("AI: ", value=response, height=300)
    else:
        st.warning("กรุณากรอกข้อความ")
