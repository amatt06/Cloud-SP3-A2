table_schema = [
    {
        'AttributeName': 'title',
        'AttributeType': 'S'
    },
    {
        'AttributeName': 'artist',
        'AttributeType': 'S'
    }
]

key_schema = [
    {
        'AttributeName': 'title',
        'KeyType': 'HASH'
    },
    {
        'AttributeName': 'artist',
        'KeyType': 'RANGE'
    }
]
