import os
import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "tramdhan@gmail.com"
    password = os.getenv("GMAIL_SMTP_PWORD")

    receiver = "tramdhan@gmail.com"
    context = ssl.create_default_context(cafile="./venv/lib/python3.12/site-packages/certifi/cacert.pem")

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
