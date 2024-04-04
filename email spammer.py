import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

def send_email(sender_email, app_password, recipient_email, subject, body):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(message)
    print("Email sent")

if __name__ == "__main__":
    sender_email = "YOUR GMAIL"
    app_password = "GMAIL APP PASSWORD" 

    with open("recipient_emails.txt", "r") as file:
        recipient_emails = file.readlines()

    subject = "subject"
    body = "body"
    while True:
        for recipient_email in recipient_emails:
            recipient_email = recipient_email.strip()
            send_email(sender_email, app_password, recipient_email, subject, body)
            time.sleep(0)