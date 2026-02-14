import streamlit as st
from mashup import create_mashup
import os
import smtplib
from email.message import EmailMessage

# 🔐 YOUR EMAIL CONFIG (CHANGE THESE)
SENDER_EMAIL = "parralexpie@gmail.com"
APP_PASSWORD = "wkfp qytg woeu tpai"

st.set_page_config(
    page_title="Songs Mashup Generator",
    page_icon="🎵",
    layout="centered"
)

st.title("🎵 Songs Mashup Generator")

singer_name = st.text_input("🎤 Singer Name")
num_videos = st.slider("🎶 Number of Songs", 1, 20, 5)

length_option = st.radio(
    "🎧 Select Audio Length",
    ["Custom Duration", "Full Song"]
)

if length_option == "Custom Duration":
    duration = st.slider("⏱ Duration per Song (seconds)", 5, 30, 10)
else:
    duration = 0

output_filename = st.text_input("📁 Output File Name", "mashup")
receiver_email = st.text_input("📧 Enter Email to Receive ZIP")

def send_email(receiver_email, zip_path):
    msg = EmailMessage()
    msg['Subject'] = "🎵 Your Mashup is Ready!"
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver_email
    msg.set_content("Hi!\n\nYour mashup file is attached.\nEnjoy 🎧")

    with open(zip_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(zip_path)

    msg.add_attachment(file_data,
                       maintype='application',
                       subtype='zip',
                       filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)

if st.button("Generate Mashup 🎧"):

    if singer_name and output_filename and receiver_email:

        with st.spinner("Creating your mashup..."):
            mp3_file, zip_file, error = create_mashup(
                singer_name,
                num_videos,
                duration,
                output_filename
            )

        if error:
            st.error(error)

        elif mp3_file and os.path.exists(mp3_file):

            st.success("Mashup Created Successfully! 🎉")

            st.audio(mp3_file)

            with open(zip_file, "rb") as file:
                st.download_button(
                    label="Download ZIP 📦",
                    data=file,
                    file_name=os.path.basename(zip_file),
                    mime="application/zip"
                )

            # 🔥 Send Email
            try:
                send_email(receiver_email, zip_file)
                st.success("ZIP file sent to email successfully! 📧")
            except Exception as e:
                st.error(f"Email failed: {str(e)}")

        else:
            st.error("Unknown error occurred.")

    else:
        st.warning("Please fill all fields.")
