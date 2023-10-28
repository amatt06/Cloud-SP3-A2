from flask import Flask
from utilities.setup import setup_data
from app.controller.login_handler import handle_login

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")


@app.route('/')
def login():
    return handle_login()


if __name__ == '__main__':
    if setup_data():
        app.run(debug=True)
    else:
        print("Error! Setup Unsuccessful")
