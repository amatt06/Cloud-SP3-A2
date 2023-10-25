import json
import boto3
from schemas.music_table_schema import table_schema, key_schema

dynamodb = boto3.resource('dynamodb')

table_name = 'music'


def create_music_table():
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


def load_data():
    create_music_table()
    with open('data/a2.json', 'r') as json_file:
        data = json.load(json_file)

    songs = data.get('songs', [])

    table = dynamodb.Table(table_name)
    for item in songs:
        table.put_item(Item=item)

    print("Data Loaded")
