import mysql.connector

def fetch_data():
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

        # SQL query to fetch data
        select_data_query = "SELECT * FROM students;"

        # Execute the SQL query
        cursor.execute(select_data_query)

        # Fetch all rows returned by the query
        rows = cursor.fetchall()

        # Check if any rows exist
        if rows:
            print("Data in students table:")
            for row in rows:
                print(row)  # Each row returned is a tuple of column values
        else:
            print("No data found in table.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        db.close()

# Call the function to fetch data
fetch_data()
