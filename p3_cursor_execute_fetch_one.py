import mysql.connector

# Create connection to MySQL
db = mysql.connector.connect(
    option_files="config.ini")

# Instantiate the cursor
cursor = db.cursor()
#cursor = db.cursor(dictionary=True) # тогда можно писать city["Name"]...
#cursor = db.cursor(named_tuple=True) # тогда можно писать city.Name ...


# Execute the query
cursor.execute("""SELECT Name, CountryCode,
                Population
                FROM city.city
                WHERE Population > 9000000
                ORDER BY Population DESC"""
                )

print(__file__ + " - Using the default cursor:")
print("")
if cursor.with_rows:
    print("{0:15s}{1:8s}{2:5s}".format(
            "City", "Country", "Pop"
        )
    )
city = cursor.fetchone()
while city:
    print("{0:15s}{1:^7s}{2:4.1f}".format(
            city[0],
            city[1],
            city[2]/1000000.0
        )
    )
    city = cursor.fetchone()
cursor.close()
db.close()