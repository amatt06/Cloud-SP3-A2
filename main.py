from flask import Flask, render_template
from utilities.setup import setup_data
from app.controller.login_handler import handle_login
from app.controller.registration_handler import handle_registration

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")


@app.route('/', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/handle_login', methods=['POST'])
def post_login():
    return handle_login()


@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/handle_register', methods=['POST'])
def post_register():
    return handle_registration()


@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


if __name__ == '__main__':
    if setup_data():
        app.run(debug=True)
    else:
        print("Error! Setup Unsuccessful")
