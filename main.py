import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

sender   = os.getenv("MAIL_USER")
password = os.getenv("MAIL_PASS")
receiver = os.getenv("MAIL_TO")
file_path = "grass.png"

msg = MIMEMultipart()
msg["From"]    = sender
msg["To"]      = receiver
msg["Subject"] = os.getenv("MAIL_SUBJECT")

with open(file_path, "rb") as f:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(f.read())
encoders.encode_base64(part)
part.add_header("Content-Disposition", f'attachment; filename="{file_path}"')
msg.attach(part)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
