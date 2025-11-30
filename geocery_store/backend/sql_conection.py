import mysql.connector

__cnx = None

def get_sql_conection(): 
    global __cnx

    if __cnx is None:
        __cnx = mysql.connector.connect(
            user="asad1122",
            password="asad1122",
            host="127.0.0.1",
            database="gs"
        )

    return __cnx
