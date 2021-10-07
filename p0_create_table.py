import sys
import mysql.connector

try:
    db = mysql.connector.connect(
        option_files="config.ini")
except:
    print("Connection with Base Data error!")
    sys.exit(1)

cursor = db.cursor()
cursor.execute("""
    create table abonent (
    id int primary key auto_increment not null,
    name varchar(20),
    address varchar(30))
    """)