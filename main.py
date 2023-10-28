from flask import Flask, render_template
from utilities.setup import setup_data

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")


@app.route('/')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    if setup_data():
        app.run(debug=True)
    else:
        print("Error! Setup Unsuccessful")
