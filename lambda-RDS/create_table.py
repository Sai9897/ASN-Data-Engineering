import mysql.connector

def create_table():
    # Configure the connection
    db = mysql.connector.connect(
        host="YOUR RDS END POINT",
        user="YOUR USER NAME",
        password="YOUR PASSWORD",
        database="YOUR DATABASE NAME"
    )

    # Create a cursor object
    cursor = db.cursor()

    # SQL statement to create a table
    create_table_sql = """CREATE TABLE YOUR_TABLE_NAME (
                             id INT AUTO_INCREMENT PRIMARY KEY,
                             first_name VARCHAR(50),
                             last_name VARCHAR(50),
                             phone VARCHAR(15),
                             organization varchar(30),
                             technology Varchar(50)
                          );"""

    try:
        # Execute the SQL command
        cursor.execute(create_table_sql)
        print("Table created successfully")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        db.close()

# Call the function to create the table
create_table()
