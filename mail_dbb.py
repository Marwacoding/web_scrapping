# https://www.jcchouinard.com/python-automation-with-cron-on-mac/
# https://www.mysqltutorial.org/mysql-delete-duplicate-rows/
# https://stackoverflow.com/questions/6107167/mysql-delete-duplicate-records-but-keep-latest
import file_db
import mysql.connector



mydb = mysql.connector.connect (
            host="scrap_sql",
            user="root",
            database = "my_db",
            password="123",
            )
c = mydb.cursor(buffered=True)


def remove_carpet_duplicate():
    c.execute("DELETE FROM carpet WHERE id NOT IN (SELECT * FROM (SELECT MIn(id) FROM carpet GROUP BY carpet_description, carpet_price, carpet_name) as del_duplicate)")
    mydb.commit()

def remove_mirror_duplicate():
    c.execute("DELETE FROM mirror WHERE id NOT IN (SELECT * FROM (SELECT MIn(id) FROM mirror GROUP BY mirror_description, mirror_price, mirror_named) as mirror_duplicate)")
    mydb.commit()

# def remove_duplicate():
#     c.execute("DELETE FROM carpet WHERE id IN (SELECT  * FROM ( SELECT MIN(id) FROM carpet GROUP BY carpet_description, carpet_name, carpet_price HAVING COUNT(carpet_description) > 1) as temp)")
#     mydb.commit()


def select_carpet_time():
    c.execute("SELECT * FROM carpet WHERE DATE_ADD(carpet_date, INTERVAL 12 HOUR) >= NOW()")
    mydb.commit()

def select_mirror_time():
    c.execute("SELECT * FROM mirror WHERE DATE_ADD(mirror_date, INTERVAL 40 HOUR) >= NOW()")
    mydb.commit()
#print('time selector', select_time())

remove_carpet_duplicate()
#remove_mirror_duplicate()
select_carpet_time()