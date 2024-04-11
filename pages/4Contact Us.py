import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(name, email):
    # Set up SMTP server and login credentials (replace with your SMTP server details)
    smtp_server = 'smtp.yourserver.com'
    smtp_port = 587
    smtp_username = 'your_email@example.com'
    smtp_password = 'your_email_password'

    # Create a message object
    message = MIMEMultipart()
    message['From'] = smtp_username
    message['To'] = email
    message['Subject'] = 'Form Submission'

    # Create email body
    body = f"Hello {name},\n\nThank you for submitting the form!\n\nBest regards,\nYour Team"
    message.attach(MIMEText(body, 'plain'))

    # Connect to SMTP server and send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, email, message.as_string())

def main():
    st.title("Contact Form")

    name = st.text_input("Name:")
    email = st.text_input("Email:")

    if st.button("Send"):
        if name and email:
            send_email(name, email)
            st.success("Form submitted successfully! Check your email.")
        else:
            st.warning("Please fill out all fields.")

if __name__ == "__main__":
    main()