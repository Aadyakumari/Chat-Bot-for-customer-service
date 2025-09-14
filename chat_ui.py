import requests
import streamlit as st

st.title("Customer Service Chatbot 🤖")stream

user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        response = requests.get("http://127.0.0.1:5000/get", params={"msg": user_input})
        bot_reply = response.json()["response"]
        st.text_area("Bot:", bot_reply, height=100)

