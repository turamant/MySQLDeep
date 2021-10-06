from mysql.connector import MySQLConnection, Error


def query_with_fetchone():
    try:
        conn = MySQLConnection(
            option_files="config.ini"
        )
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM city
        """)

        rows = cursor.fetchall()
        count = cursor.rowcount  # свойство объекта cursor
        print("Всего строк: ", count)

        for row in rows:
            print(row)


    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    query_with_fetchone()