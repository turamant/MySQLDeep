from mysql.connector import MySQLConnection, Error


def query_with_fetchone():
    try:
        conn = MySQLConnection(
            option_files="config.ini"
        )
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM city LIMIT 3
        """)

        row = cursor.fetchone()

        while row is not None:
            print(row)
            row = cursor.fetchone()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    query_with_fetchone()