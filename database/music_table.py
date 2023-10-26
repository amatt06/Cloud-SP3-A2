import boto3
from schemas.music_table_schema import table_schema, key_schema
from data.data_loader import load_music_data

dynamodb = boto3.resource('dynamodb')

table_name = 'music'


def create_music_table():
    existing_tables = dynamodb.meta.client.list_tables()
    if table_name in existing_tables['TableNames']:
        return True
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
            return True
        except Exception as e:
            print(str(e))
            return False


def load_data():
    try:
        data = load_music_data()
        songs = data.get('songs', [])

        table = dynamodb.Table(table_name)
        for item in songs:
            table.put_item(Item=item)
        return True
    except Exception as e:
        print({str(e)})
        return False
