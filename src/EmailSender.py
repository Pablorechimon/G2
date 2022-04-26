# https://medium.com/@mamir.khan/send-secure-emails-using-python-in-few-lines-of-code-d7605f20e43c

# Now rest of the code
import email, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls() # to make emails encrypted
s.login("youremail@gmail.com", "your-password")
msg["Subject"] = "My Subject" # subject of your email
msg["From"] = "sender@gmail.com"
msg["To"] = 'recipient-1@email.com,recipient-2@email.com'
msg["Cc"] = "serenity@example.com,inara@example.com"
body = MIMEText("SMTP Sample Email Body")
msg.attach(body)
s.sendmail(msg["From"], msg["To"].split(","), msg.as_string())
s.quit()