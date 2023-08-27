import mysql.connector

def insert_data(rows):
    try:
        # Configure the connection
        db = mysql.connector.connect(
            host="testdb.ckk2y86it138.us-east-1.rds.amazonaws.com",
            user="admin",
            password="Amazon91",
            database="test_database"
        )

        # Create a cursor object
        cursor = db.cursor()

        # SQL query to insert data
        insert_data_query = """INSERT INTO students (first_name, last_name, phone, organization, technology)
                                VALUES (%s, %s, %s, %s, %s);"""

        # Execute the SQL query with multiple rows
        cursor.executemany(insert_data_query, rows)

        # Commit the transaction
        db.commit()

        print(f"{cursor.rowcount} rows inserted.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        db.close()

# Sample data (list of tuples)
rows = [
    ('John', 'Doe', '1234567890', 'ABC Corp', 'Python'),
    ('Jane', 'Doe', '0987654321', 'XYZ Corp', 'Java')
]

# Call the function to insert multiple rows
insert_data(rows)
