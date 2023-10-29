from flask import Flask, render_template, session, request
import os
from utilities.setup import setup_data
from app.controller.login_handler import handle_login
from app.controller.registration_handler import handle_registration
from app.controller.query_handler import handle_query

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")
app.secret_key = os.urandom(24)


@app.route('/', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/handle_login', methods=['POST'])
def post_login():
    return handle_login()


@app.route('/main')
def main():
    user_name = session.get('user_name')
    message = request.args.get('message', None)
    music_items = request.args.get('music_items', None)
    return render_template('main.html', user_name=user_name, message=message, music_items=music_items)


@app.route('/query', methods=['POST'])
def post_query():
    return handle_query()


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
