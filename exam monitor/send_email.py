import smtplib
from email.message import EmailMessage
import os

def send_email_alert(subject, body, attachments=[]):
    smtp_server = "smtp.mailtrap.io"
    smtp_port = 2525
    smtp_user = "f7e79c2aec81bd"
    smtp_pass = "57e953a127fcb1"

    sender_email = "monitor@alliance.com"
    recipient_email = "faculty@alliance.edu"

    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.set_content(body)  # ✅ Make sure body is added first

    for path in attachments:
        try:
            with open(path, "rb") as f:
                data = f.read()
                msg.add_attachment(
                    data,
                    maintype="application",
                    subtype="octet-stream",
                    filename=os.path.basename(path)
                )
        except Exception as e:
            print(f"❌ Failed to attach {path}: {e}")

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.send_message(msg)
            print("✅ Email sent successfully with body and attachments.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
