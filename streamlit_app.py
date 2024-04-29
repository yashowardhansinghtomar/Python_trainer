# Import necessary modules
import google.generativeai as genai
import streamlit as st

# Implement API Key 
genai.configure(api_key="AIzaSyA6e5nc9Xq2Y4mSbyw3OIHl05_w2WVGcIo")

st.title("Python Trainer")
# Declaring the prompt 
prompt= st.text_input("Ask me anything")
# Create a submit button
submit_button = st.button("Submit")
# Contextualizing the prompt
context_prompt = f"Act as an experienced technical trainer , who focuses in python and machine learning , give proper definitions , points to remember , code examples and summary on the topic {prompt}"

# Creating Model and Testing Prompt
model = genai.GenerativeModel('gemini-1.0-pro-latest')
response = model.generate_content(context_prompt)

# If the submit button is clicked, display the chatbot's response
if submit_button:
    st.write(response.text)