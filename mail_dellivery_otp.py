import secrets
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def generate_otp(length=6):
    characters = string.digits
    otp = ''.join(secrets.choice(characters) for i in range(length))
    return otp

def send_otp(email, otp):
    # Email server configuration
    mail_auth_token_value = os.getenv("mail_auth_token")
    mail_id_auth_value = os.getenv("mail_id_token")
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = mail_id_auth_value
    sender_password = mail_auth_token_value

    # Create the email content
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = email
    message['Subject'] = 'Your OTP Code'

    body = f'Your OTP code is {otp}'
    message.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)
        text = message.as_string()
        server.sendmail(sender_email, email, text)
        server.quit()
        print(f'OTP sent successfully to {email}')
    except Exception as e:
        print(f'Failed to send OTP: {e}')

# Example usage
def verify_otp(input_otp, actual_otp):
    return input_otp == actual_otp
