from email.message import EmailMessage
import smtplib
import os
import random
from dotenv import load_dotenv
from quote import quote
#this program will allow a user to send a gmail email with a custom body or a shakespear quote
load_dotenv(".env")
#prompting user for their email address and password to connect the server to it
user_name = input("Enter your gmail: ") 
gmail_password = input("Enter your gmail password: ") 

SENDER = os.environ.get(user_name)
PASSWORD = os.environ.get(gmail_password)

#logins to the email and sends the email
def send_email(recipient, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = SENDER
    msg["To"] = recipient
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(SENDER, PASSWORD)
    server.send_message(msg)
    server.quit()
#generating shakespeare quote
quotes = quote("William Shakespeare", limit=50)
body_quote = random.sample(quotes, k=1)[0]['quote']

#prompting for email subject, recipient and body text
email_subject = input("Enter your email subject: ") 
recipient = input("Enter the email of who you are emailing: ")
body = input("Enter your email body, or type W to send a random Shakespeare quote: ") 

#depending on what they want to send as their body text
if body.lower() == "w":
	send_email(recipient, subject=email_subject, body=body_quote)
else:
	send_email(recipient, subject=email_subject, body=body)

