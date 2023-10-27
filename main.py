from utilities import setup
from app.app import run

if __name__ == '__main__':
    if setup.setup_data():
        run()
    else:
        print("Setup Unsuccessful")
