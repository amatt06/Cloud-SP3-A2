from flask import Flask, render_template
from utilities.setup import setup_data
from app.controller.login_handler import handle_login
from app.controller.registration_handler import handle_registration

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")


@app.route('/')
def login():
    return handle_login()


@app.route('/register')
def register():
    return handle_registration()


if __name__ == '__main__':
    if setup_data():
        app.run(debug=True)
    else:
        print("Error! Setup Unsuccessful")
