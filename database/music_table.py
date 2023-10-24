import boto3
from schemas.music_table_schema import table_schema, key_schema

dynamodb = boto3.resource('dynamodb')

table_name = 'music'


def create_music_table():
    # Check if the table already exists
    existing_tables = dynamodb.meta.client.list_tables()
    if table_name in existing_tables['TableNames']:
        print("Music Table Already Exists.")
    else:
        try:
            dynamodb.create_table(
                TableName=table_name,
                KeySchema=key_schema,
                AttributeDefinitions=table_schema,
                ProvisionedThroughput={
                    'ReadCapacityUnits': 10,
                    'WriteCapacityUnits': 10
                }
            )
            print("Music Table Created Successfully")
        except Exception as e:
            print(str(e))
