from database import music_table
from utilities import artist_image_util
from utilities.table_utils import check_table_status


def setup():
    if music_table.create_music_table():
        if check_table_status(music_table.table_name):
            if music_table.load_data():
                result = artist_image_util.upload_images()
                if result:
                    return True
                else:
                    print("Error: Uploading Images Failed.")
            else:
                print("Error: Loading Data Failed.")
        else:
            print("Table Not Found")
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
