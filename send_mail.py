import smtplib, ssl  # smtplib buit-in de Python SMTP protocol client that allows us to connect to our email account and send mail via SMTP.
from email.mime.text import MIMEText  # MIME (Multipurpose Internet Mail Extensions) is a standard for formatting files to be sent over the internet so they can be viewed in a browser or email application.
from email import encoders

def send_email():

    body_of_email = "test"

    msg = MIMEText(body_of_email, "html")
    msg["Subject"] = "Something new wes added to your Maison Du Monde db"
    msg["From"] = "marwa.tocode@gmail.com"
    msg["To"] = "majbrim@gmail.com"

    s = smtplib.SMTP_SSL(host = "smtp.gmail.com", port = 465)
    s.login(user = "marwa.tocode@gmail.com", password = "Pharma1$")
    s.sendmail(sender, receiver, msg.as_string())
    s.quit()

send_email()