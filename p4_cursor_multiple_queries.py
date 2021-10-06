import mysql.connector

# Format strings
FMT_QUERY = "Query {0}:\n" + "-"*8
FMT_HEADER = "{0:18s}  {1:7s}  {2:3s}"
FMT_ROW = "{0:18s}  {1:^7s}   {2:4.1f}"

db = mysql.connector.connect(
    option_files="config.ini"
)

# Define the queries
sql_select = """
    SELECT Name, CountryCode, Population
    FROM world.city
    WHERE CountryCode = %s
    ORDER_BY Population DESC
    LIMIT 3 """

sql_do = "DO SLEEP(3)"
queries = [sql_select, sql_do, sql_select]

cursor = db.cursor()

results = cursor.execute(
    ";".join(queries),
    params=("USA", "IND"),

)

count = 0

for result in results:
    count += 1
    print(FMT_QUERY.format(count))
    if result.with_rows:
        print(FMT_HEADER.format(
            "City", "Country", "Pop"
        ))
        city = cursor.fetchone()
        while city:
            print(FMT_ROW.format(
                city[0],
                city[1],
                city[2] / 1000000
            ))
            city = cursor.fetchone()
    else:
        print("No result to print")
    print("")
cursor.close()
db.close()
