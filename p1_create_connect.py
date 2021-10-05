import sys
import mysql.connector

try:
    db1 = mysql.connector.connect(
        option_files="config.ini")

    # db1 = mysql.connector.MySQLConnection(
    #    option_files="config.ini")

    # db1 = mysql.connector.MySQLConnection()
    # db1.connect(option_files="config.ini")

    # db1 = mysql.connector.MySQLConnection()
    # db1.config(option_files="config.ini")
    # db1.connect()

    print("Успешное соединение с БД ")
    print("MySQL connection ID for db2: {0}".format(db1.connection_id))

except:
    print("Connection with Base Data error!")
    sys.exit(1)

cursor = db1.cursor()
try:
    cursor.execute("SELECT ID, Name from city")
    print("ID\tName")
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        print("%d\t\t\t%s" % (row[0], row[1]))
except:
    print("error in fetching(выборка) rows")
    # sys.exit(1)

print("Second variant")
try:
    cursor.execute("SELECT ID, Name from city")
    print("ID\tName")
    rows = cursor.fetchall()
    for row in rows:
        print("%d\t\t\t%s" % (row[0], row[1]))
except:
    print("Error fetching rows")
    # sys.exit(1)

cursor.close()
print("MySQL connection ID for db2: {0}".format(db1.connection_id))
db1.close()