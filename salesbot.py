import transformers
from transformers import GoogleBard
import streamlit as st
from streamlit_chat import message
import config
import os
os.environ["OPENAI_API_KEY"] = config.openAI

# Define the personality of the salesbot
age = st.sidebar.number_input("Age", 25, 50)
work_experience = st.sidebar.number_input("Work experience (years)", 1, 10)
projects = st.sidebar.text_input("Previous projects", "e.g., Salesforce, HubSpot, Marketo")

# Create the salesbot
bot = GoogleBard(
    api_key=config.openAI,
    embeddings="openai",
    prompt="I am a salesbot with",
    age=age,
    work_experience=work_experience,
    projects=projects,
)

# Start the chat
st.title("Salesbot")
while True:
    message = st.text_input("What can I help you with?")
    response = bot.generate_response(message)
    st.write(response)
