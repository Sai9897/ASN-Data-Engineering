import mysql.connector

def create_database():
    try:
        # Configure the connection
        db = mysql.connector.connect(
            host="YOUR RDS END POINT",
            user="YOUR USER NAME",
            password="YOUR PASSWORD"
        )

        # Create a cursor object
        cursor = db.cursor()

        # SQL query to create a new database
        create_database_query = "CREATE DATABASE IF NOT EXISTS YOUR DATABASE NAME;"

        # Execute the SQL query
        cursor.execute(create_database_query)

        print("Database created successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        db.close()

# Call the function to create the database
create_database()
