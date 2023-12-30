import streamlit as st
from send_email import send_email
import pandas

df = pandas.read_csv("data/topics.csv")

st.header("Contact Us!")

with st.form(key="contact_us_form"):
    user_email = st.text_input("Your email")
    option = st.selectbox("Select a topic", df["topic"])
    form_message = st.text_area("Message")
    message = f"""\
Subject: {option} from {user_email}
From: {user_email}
topic: {option}
{form_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        print(button)  # boolean
        send_email(message)
        st.info("Email sent!")