
# import file_db
# import postgres
#import mysql.connector

import smtplib, ssl
from email.mime.text import MIMEText
from email import encoders

import os
from dotenv import load_dotenv
load_dotenv()


def send_email(def_time, mail=str):
    
    body_of_email = "".join(str(def_time))
    #print('this is most recent time',def_time)
    sender = os.environ["mail_pw"]
    receiver= mail

    msg = MIMEText(body_of_email, "html")
    msg["Subject"] = "Maison du Monde API"
    msg["From"] = os.environ["mail_pw"]
    msg["To"] =  mail

    s = smtplib.SMTP_SSL(host = "smtp.gmail.com", port = 465)
    s.login(user = os.environ["mail_pw"], password = os.environ["pw_mail"])
    s.sendmail(sender, receiver, msg.as_string())
    s.quit()

