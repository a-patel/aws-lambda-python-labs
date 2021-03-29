import boto3
import botocore
import json
import logging
import os
import pymysql


log = logging.getLogger()
log.setLevel(logging.INFO)


logger = logging.getLogger()
logger.setLevel(logging.INFO)


# settings
db_host = os.db_host
db_username = os.db_username
db_password = os.db_password
db_name = os.db_name
customer_name = os.customer_name

try:
    conn = pymysql.connect(db_host, user=db_username, passwd=db_password, db=db_name, connect_timeout=5)
except Exception as e:
    logger.error(e)
    raise e

logger.info("SUCCESS: Connection to RDS mysql instance succeeded")


# This function fetches content from MySQL RDS instance
def lambda_handler(event, context):
    log.debug('Event: %s', event)
    print("Received event: " + json.dumps(event, indent=2))


    # insert data
    item_count = 0

    with conn.cursor() as cur:
        cur.execute("create table customer (Id  int NOT NULL, Name varchar(255) NOT NULL, PRIMARY KEY (Id))")
        cur.execute('insert into customer (Id, Name) values(1, "Eminem")')
        cur.execute('insert into customer (Id, Name) values(2, "Drake")')
        cur.execute('insert into customer (Id, Name) values(3, "Jay Z")')
        conn.commit()
        cur.execute("select * from customer")
        for row in cur:
            item_count += 1
            logger.info(row)

    print(f'Added {item_count} items from RDS MySQL table')


    # get data
    cursor = conn.cursor()
    sql = "select name from customer where Name='"+customer_name+"'"
    response = {}
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        response['status']=200
        response['name']=result[0]['name']
        response['message']="Status OK"
        
    except:
        response['status']=404
        response['name']="-"
        response['message']="Name Not Found"
        
    print(str(response))


    return 0