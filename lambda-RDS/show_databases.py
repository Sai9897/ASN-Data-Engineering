import mysql.connector

try:
    # Configure the connection
    db = mysql.connector.connect(
        host="YOUR RDS END POINT",
        user="YOUR USER NAME",
        password="YOUR PASSWORD"
    )

    # Create a cursor object
    cursor = db.cursor()

    # SQL query to show databases
    show_databases_query = "SHOW DATABASES;"

    # Execute the SQL query
    cursor.execute(show_databases_query)

    # Fetch all rows returned by the query
    databases = cursor.fetchall()

    # Print each database name
    for database in databases:
        print(database[0])  # Each row returned is a tuple, so access the first element

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    cursor.close()
    db.close()
