# https://medium.com/@mamir.khan/send-secure-emails-using-python-in-few-lines-of-code-d7605f20e43c

# Now rest of the code
import email, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64


def send_email(to, subject, cc, content):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls() # to make emails encrypted
    s.login("youremail@gmail.com", "your-password")
    
    msg["Subject"] = subject # subject of your email
    msg["From"] = "sender@gmail.com"
    msg["To"] = to
    msg["Cc"] = cc # to string
    
    body = content # MIMEText("SMTP Sample Email Body")
    msg.attach(body)
    
    s.sendmail(msg["From"], msg["To"].split(","), msg.as_string())
    s.quit()