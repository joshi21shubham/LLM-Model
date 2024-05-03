from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure Google GenerativeAI with API key
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Function to start chat session and get response
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini Application")

# Input box for user question
input_text = st.text_input("Input:")

# Button to submit the question
submit_button = st.button("Ask the question")

# If submit button is clicked
if submit_button:
    # Check if input is provided
    if input_text:
        # Get response from Gemini model
        response_chunks = get_gemini_response(input_text)
        # Display the response
        st.subheader("The Response is")
        for chunk in response_chunks:
            st.write(chunk.text)
            st.write("_" * 80)
        # Display chat history
        st.subheader("Chat History")
        st.write(chat.history)
    else:
        st.write("Please provide a question.")
