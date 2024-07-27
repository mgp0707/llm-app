import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send email
def send_email(subject, message, sender_email, receiver_email, password):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        return True
    except Exception as e:
        st.error(f"Failed to send email. Error: {e}")
        return False

# Set the title of the web page
st.set_page_config(page_title="Daniel Park's Portfolio", layout='wide')

# Header section with your name and introduction
st.title("Daniel Park's Portfolio")
st.image("face.png", width=150)  # Add your photo here
st.write("""
# Hello, I'm Daniel Park!
Welcome to my portfolio website where I showcase various large language model (LLM) services that I have developed and worked with. 
I am passionate about natural language processing and artificial intelligence, and I am excited to share my projects with you. 
Feel free to explore the different sections to learn more about each service.
""")

# Contact form
st.write("## Contact Me")
with st.form(key='contact_form'):
    name = st.text_input("Name")
    email = st.text_input("Email")
    subject = st.text_input("Subject")
    message = st.text_area("Message")
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if name and email and subject and message:
            sender_email = 'phantomglix@gmail.com'  # Replace with your email
            sender_password = 'sjmb1709'  # Replace with your email password or use an app-specific password
            receiver_email = 'djdanx7@gmail.com'
            email_message = f"Name: {name}\nEmail: {email}\n\n{message}"
            
            if send_email(subject, email_message, sender_email, receiver_email, sender_password):
                st.success("Your message has been sent successfully!")
            else:
                st.error("Failed to send your message. Please try again later.")
        else:
            st.error("Please fill in all fields before submitting.")


# Footer
st.markdown("""
---
© 2024 Daniel Park. All rights reserved.
""")
