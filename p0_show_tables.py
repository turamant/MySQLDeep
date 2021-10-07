import sys
import mysql.connector

try:
    db = mysql.connector.connect(
        option_files="config.ini")
except:
    print("Connection with Base Data error!")
    sys.exit(1)

SQL1 = """SHOW TABLES;"""

SQL2 = """SHOW CREATE TABLE world.city;"""
#SQL2 = """SHOW CREATE TABLE world.country;"""
#SQL2 = """SHOW CREATE TABLE world.city;"""

#SQL3 = """SELECT table_name FROM information_schema.tables;"""
SQL4 = """SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_NAME = 'city'; """

# Execute a query

cursor = db.cursor()

print("SQL1 - Показать все таблицы из БД")
if SQL1:
    cursor.execute(SQL1)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

print("\nSQL2 - Показать параметры таблицы")
if SQL2:
    cursor.execute(SQL2)
    row = cursor.fetchone()
    while row is not None:
        print(row[0])
        print(row[1])
        row = cursor.fetchone()

print("\nSQL3 - Показать параметры таблицы")
if SQL3:
    cursor.execute(SQL3)
    rows = cursor.fetchall()
    for row in rows:
        print(row[0])

print("\nSQL4 - Показать параметры колонок таблицы")
if SQL4:
    cursor.execute(SQL4)
    rows = cursor.fetchall()
    for row in rows:
        print(row[0])





db.close()