from flask import Flask, render_template
from utilities.setup import setup_data

app = Flask(__name__)

if __name__ == '__main__':
    if setup_data():
        app.run(debug=True)
    else:
        print("Error! Setup Unsuccessful")
