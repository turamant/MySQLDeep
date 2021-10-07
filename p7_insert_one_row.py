from mysql.connector import MySQLConnection, Error


def insert_abonent(name, address):
    query = """INSERT INTO abonent(
                    name, address)
                    VALUES(%s,%s)"""
    args = (name, address)
    print(*args)
    try:
        conn = MySQLConnection(
            option_files="config.ini"
        )
        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('Last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def main():
    name = str(input("Введите имя: "))
    address = str(input("ВВедите адресс: "))
    insert_abonent(name, address)

if __name__ == '__main__':
    main()