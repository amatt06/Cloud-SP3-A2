import json


def load_music_data():
    with open('data/a2.json', 'r') as json_file:
        data = json.load(json_file)
    return data
