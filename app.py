import streamlit as st
import nltk 
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK resources
nltk.download("punkt")
nltk.download("stopwords")

# Load the GPT-based chatbot model
chatbot = pipeline("text-generation", model="distilgpt2")

def healthcare_chatbot(user_input):
    user_input = user_input.lower()  # Normalize input

    if "symptom" in user_input:
        return "Please consult a doctor for accurate advice."
    elif "appoint" in user_input:
        return "Would you like to schedule an appointment with the doctor?"
    elif "medication" in user_input:
        return "It's important to take prescribed medicines regularly."
    else:
        response = chatbot(user_input, max_length=100, num_return_sequences=1)
        return response[0]['generated_text']

def main():
    st.title("Healthcare Assistant Chatbot")
    
    user_input = st.text_input("How can I assist you today?")
    
    if st.button("Submit"):
        if user_input:
            st.write("**User:**", user_input)
            
            # Corrected st.spinner usage
            with st.spinner("Processing your query... please wait"):
                response = healthcare_chatbot(user_input)
            
            st.write("**Healthcare Assistant:**", response)
        else:
            st.write("Please enter a message to get a response.")
            
# Run the Streamlit app
if __name__ == "__main__":
    main()
