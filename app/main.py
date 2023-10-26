from database.music_table import create_music_table, load_data
from utilities.artist_image_util import upload_images


def setup():
    if create_music_table():
        if load_data():
            result = upload_images()
            if result:
                return True
            else:
                print("Error: Uploading Images Failed.")
        else:
            print("Error: Loading Data Failed.")
    else:
        print("Error: Creating Music Table Failed.")

    return False


def run():
    print("Running App...")


if __name__ == '__main__':
    if setup():
        run()
    else:
        print("Setup Unsuccessful")
