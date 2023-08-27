import mysql.connector

try:
    # Configure the connection
    db = mysql.connector.connect(
        host="YOUR RDS END POINT",
        user="YOUR USER NAME",
        password="YOUR PASSWORD",
        database="YOUR DATABASE NAME"
    )

    # Create a cursor object
    cursor = db.cursor()

    # SQL query to show databases
    show_tables_query = "SHOW TABLES;"

    # Execute the SQL query
    cursor.execute(show_tables_query)

    # Fetch all rows returned by the query
    tables = cursor.fetchall()

    # Print each database name
    for tables in tables:
        print(tables[0])  # Each row returned is a tuple, so access the first element

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    cursor.close()
    db.close()
