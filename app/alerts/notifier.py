import os
import smtplib
from email.mime.text import MIMEText

def send_email_alert(message):
    if os.getenv("EMAIL_ALERTS") != "True":
        return

    msg = MIMEText(message)
    msg["Subject"] = "LeakSentinel Alert"
    msg["From"] = os.getenv("SMTP_EMAIL")
    msg["To"] = os.getenv("SMTP_EMAIL")

    with smtplib.SMTP(os.getenv("SMTP_SERVER"), int(os.getenv("SMTP_PORT"))) as server:
        server.starttls()
        server.login(os.getenv("SMTP_EMAIL"), os.getenv("SMTP_PASSWORD"))
        server.send_message(msg)