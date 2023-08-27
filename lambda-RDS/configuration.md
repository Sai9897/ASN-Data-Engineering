[create_database.py](..%2F..%2Fmock-speak-data-eng%2FLambda-Rds%2Fcreate_database.py)aws lambda update-function-configuration \
--function-name YOUR_FUNCTION_NAME \
--environment "Variables={DB_HOST=YOUR_RDS_ENDPOINT,DB_USER=YOUR_RDS_USERNAME,DB_PASSWORD=YOUR_RDS_PASSWORD,DB_DATABASE=YOUR_RDS_DBNAME}"