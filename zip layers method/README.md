## making mysql and rds layer zip
    mkdir layer(YOUR LAYER NAME)
    cd layer
    pip install mysql-connector-python -t ./python
    cp -r rds layer/python(CHECK PATH)
    zip -r test.zip ./python(CHECK PATH)

Note: copy rds folder in same place