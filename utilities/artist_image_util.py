import requests
import boto3
from io import BytesIO
from data.data_loader import load_music_data
from database import music_table

s3 = boto3.client('s3')
bucket_name = 'artist-images-bucket'


def image_exists(s3_key):
    try:
        s3.head_object(Bucket=bucket_name, Key=s3_key)
        return True
    except Exception as e:
        return False


def upload_images():
    if music_table.load_data():
        data = load_music_data()
        songs = data.get('songs', [])

        print("Uploading Images...")

        for song in songs:
            image_url = song.get('img_url')
            artist_name = song["artist"]

            if image_url:
                s3_object_key = f'artist_images/{artist_name}.jpg'

                if not image_exists(s3_object_key):
                    try:
                        response = requests.get(image_url)
                        image_data = response.content
                        s3.upload_fileobj(BytesIO(image_data), bucket_name, s3_object_key)

                    except Exception as e:
                        print(f"Error Downloading/Uploading image for {artist_name}: {str(e)}")
    else:
        print("Data Load Failed. Image Upload Canceled.")

    return True
