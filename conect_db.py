import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host='localhost',
                                         database='tiktok_account',
                                         user='root',
                                         password='root')
mycursor = connection.cursor()

def data():
    mycursor.execute("SELECT email FROM account WHERE status = 1 and type = 2 ")
    myresult = mycursor.fetchone()
    return myresult[0]    


def select_link_youtube():
    mycursor.execute("SELECT link,name,segments,id FROM links WHERE status = 0 and type = 1")
    myresult = mycursor.fetchone()
    return myresult  

def uppdate_status_link(id):
    sql_update_query = "Update links set status = 1 where id = " + str(id)
    mycursor.execute(sql_update_query)
    connection.commit()