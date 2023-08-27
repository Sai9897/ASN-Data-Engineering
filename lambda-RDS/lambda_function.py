import mysql.connector
import json
import os

def lambda_handler(event, context):
    # Retrieve database credentials from environment variables or AWS Secrets Manager
    host = os.environ.get('DB_HOST')
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASSWORD')
    database = os.environ.get('DB_DATABASE')

    # You can send the 'rows' as part of the Lambda event payload

    try:
        # Configure the connection
        db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        # Create a cursor object
        cursor = db.cursor()

        print(event)

        # SQL query to insert data
        insert_data_query = """INSERT INTO students (first_name, last_name, phone, organization, technology)
                                VALUES (%s, %s, %s, %s, %s);"""

        print(insert_data_query)

        row = (event["first_name"], event["last_name"], event["phone"], event["organization"],  event["technology"])

        print(row)

        # Execute the SQL query with multiple rows
        cursor.executemany(insert_data_query, [row])


        # Commit the transaction
        db.commit()

        return {
            'statusCode': 200,
            'body': f"{cursor.rowcount} rows inserted."
        }

    except mysql.connector.Error as err:
        return {
            'statusCode': 500,
            'body': f"Error: {err}"
        }

    finally:
        # Close the cursor and connection
        cursor.close()
        db.close()
