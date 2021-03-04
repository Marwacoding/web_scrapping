#!/usr/bin/python
# https://www.jcchouinard.com/python-automation-with-cron-on-mac/
# https://www.mysqltutorial.org/mysql-delete-duplicate-rows/
# https://stackoverflow.com/questions/6107167/mysql-delete-duplicate-records-but-keep-latest
# https://stackoverflow.com/questions/10022669/mysql-get-records-greater-than-10-hours
# https://stackoverflow.com/questions/61287796/python-mysql-connector-query-to-send-email


import file_db
import mysql.connector

import smtplib, ssl
from email.mime.text import MIMEText
from email import encoders



mydb = mysql.connector.connect (
            host="scrap_sql",
            user="root",
            database = "my_db",
            password="123",
            )
c = mydb.cursor(buffered=True)


def remove_carpet_duplicate():
    c.execute("DELETE FROM carpet WHERE id NOT IN (SELECT * FROM (SELECT MIN(id) FROM carpet GROUP BY carpet_description, carpet_price, carpet_name) as del_duplicate)")
    mydb.commit()

def remove_mirror_duplicate():
    c.execute("DELETE FROM mirror WHERE id NOT IN (SELECT * FROM (SELECT MIN(id) FROM mirror GROUP BY mirror_description, mirror_price, mirror_named) as mirror_duplicate)")
    mydb.commit()

def remove_duplicate():
    c.execute("DELETE FROM carpet WHERE id IN (SELECT  * FROM ( SELECT MIN(id) FROM carpet GROUP BY carpet_description, carpet_name, carpet_price HAVING COUNT(carpet_description) > 1) as temp)")
    mydb.commit()


def select_carpet_time():
    c.execute("SELECT * FROM carpet WHERE DATE_ADD(carpet_date, INTERVAL 12 HOUR) >= NOW()")
    return c.fetchall()
    # mycursor.execute("SELECT * FROM carpet WHERE carpet_date >= DATE_SUB(NOW(),INTERVAL 12 MINUTE);) 
    # mydb.commit()

def select_mirror_time():
    c.execute("SELECT * FROM mirror WHERE DATE_ADD(mirror_date, INTERVAL 40 HOUR) >= NOW()")
    return c.fetchall()
    # mycursor.execute("SELECT * FROM mirror WHERE mirror_date >= DATE_SUB(NOW(),INTERVAL 12 MINUTE);) 
    # mydb.commit()
#print('time selector', select_time())

def most_recent_time():
    c.execute("SELECT * FROM carpet ORDER BY carpet_date DESC LIMIT 10;")
    return c.fetchall()


def send_email(def_time):

    body_of_email = "".join(str(def_time))
    #print('this is most recent time',def_time)
    sender = "marwa.tocode@gmail.com"
    receiver= "majbrim@gmail.com"

    msg = MIMEText(body_of_email, "html")
    msg["Subject"] = "Maison du Monde API"
    msg["From"] = "marwa.tocode@gmail.com"
    msg["To"] = "majbrim@gmail.com"

    s = smtplib.SMTP_SSL(host = "smtp.gmail.com", port = 465)
    s.login(user = "marwa.tocode@gmail.com", password = "Pharma1$")
    s.sendmail(sender, receiver, msg.as_string())
    s.quit()




#remove_carpet_duplicate()
#remove_mirror_duplicate()
# #select_carpet_time()
#most_recent_time()
send_email(most_recent_time())