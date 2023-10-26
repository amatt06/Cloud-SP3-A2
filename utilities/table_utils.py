import boto3
import time


def check_table_status(table_name):
    dynamodb = boto3.client('dynamodb')
    max_retries = 10
    retries = 0

    print("Populating Table...")

    while retries < max_retries:
        response = dynamodb.describe_table(TableName=table_name)
        table_status = response['Table']['TableStatus']
        if table_status == 'ACTIVE':
            return True
        time.sleep(5)
        retries += 1

    return False
