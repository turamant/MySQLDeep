from mysql.connector import MySQLConnection, Error



def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

def query_with_fetchmany():
    try:
        conn = MySQLConnection(
            option_files="config.ini"
        )
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM city LIMIT 3
        """)

        for row in iter_row(cursor, 10):
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    query_with_fetchmany()