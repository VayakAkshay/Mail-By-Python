# -----------    Following the step to send mail by python ------------


#  1 - Go to your google account
#  2 - Open security tab
#  3 = Go to in App Password
#  4 - add the app name python and generate the password
#  5 - copy the password
#  6 - write these code 


from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'your email address'

# write password of google copied

email_password = 'ywdadkbheegezodf'
email_receiver = 'receiver address'

subject = "Hello I am Akshay Vayak"
body = """
Hello, i am python developer """
em = EmailMessage()
em['from'] = email_sender
em['to'] = email_receiver
em['subject'] = subject
em.set_content(body)
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
