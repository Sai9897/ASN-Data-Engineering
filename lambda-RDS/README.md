# Aim: Write to a RDS database using Lambda function

## Step 1:
    Create a MySQL database in RDS
        Note: 1. Set Public access to 'YES'
              2. In VPC Security groups:
                    Select the security groups and edit inbound rules to allow the rds connection from your IP address.

## Step 2:
    1. Now use your IDE to connect to the RDS database.
    2. Now open a terminal in IDE and install mysql connector.
            $ "pip install mysql-connector-python"
    3. Now create a database.
            use <create_database.py> file.
    4. To check the database that you created:
            use <show_database.py> file.
    5. Now create a table with your desired schema.
            use <create_table.py> file.
    6. To check the tables that you created:
            use <show_tables.py> file.
    7. To load data into that table:
            use <load_data.py> file.
        But our main aim is to load using lambda.

## Step 3: Creating a lambda function
    1. Create a lambda function with python as runtime.
/ For lambda to use mysql-connector, add a layer to the lambda function.

## Step 4: Creating a layer
    1. Create a Linux environment in Cloud9 IDE.
    2. Use the following commands to create a zipfile:
            mkdir mysql_layer
            cd mysql_layer
            pip install mysql-connector-python -t ./python
            zip -r mysql_layer.zip ./python
            aws lambda publish-layer-version --layer-name YOUR_LAYER_NAME  --zip-file fileb://mysql_layer.zip --compatible-runtimes YOUR_LAMBDA_RUNTIME --region TOUR_REGION
    3. Now that custom layer to your lambda function.

## Step 5: 
    1. Use <lambda_function.py> file for lambda function code source.
    2. Use <configuration.ms> file in terminal to set RDS configurations.
    3. Now deploy and test your function.
    4. To check whether the data loaded in your RDS use <check_data.py> file in IDE.

