from dotenv import load_dotenv

load_dotenv()
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(prompt, additional_info):
    model = genai.GenerativeModel('text-to-text-simple')
    response = model.generate_content([prompt, additional_info])
    return response.text

## Streamlit App

st.set_page_config(page_title="Mental Health Self-Assessment")
st.header("Let's Talk About Your Wellbeing")

# Text input for additional details (optional)
additional_info = st.text_area("Anything else you'd like to share (optional):", key="additional")

# Prompt for mental health self-assessment based on user input
prompt = f"""
You are a licensed mental health professional specializing in a variety of therapy modalities. 
A client has approached you and shared the following: {additional_info}

Based on the provided information, offer a preliminary assessment of the user's mental health 
and suggest potential resources or next steps. It's important to emphasize that this 
self-assessment is not a substitute for professional diagnosis or treatment.
"""

if st.button("Get Assessment"):
    response = get_gemini_response(prompt, additional_info.strip())
    st.subheader("Self-Assessment Insights")
    st.write(response)

# Disclaimer 
st.write("*Disclaimer: This self-assessment tool is for informational purposes only and should not be taken as a substitute for professional diagnosis or treatment. Please consult with a qualified mental health professional if you are concerned about your mental health.")
