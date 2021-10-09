import sys
import mysql.connector
import pprint

printer = pprint.PrettyPrinter(indent=1)

try:
    db = mysql.connector.connect(
        option_files="config.ini")
except:
    print("Connection with Base Data error!")

# Execute a query

result = db.cmd_query(
    """SELECT *
    FROM city.city
    WHERE ID = 130"""
)

print("Result Dictionary\n" + "=" * 17)
printer.pprint(result)
db.close()