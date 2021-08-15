from flask import *
from flask_cors import CORS
import json
import util as u

app = Flask(__name__)
app.secret_key = "#12_678_1_bhc"
CORS(app)


@app.route('/')
def index():
    return "Hello World. Welcome to Coeus Middleware :-)"


@app.route('/firmwareRunning')
def firmwareRunning():
    return json.dumps({"running": True}, indent=1)


@app.route('/getAllUsers')
def get_all_users():
    data = u.getAllSystemUsers()
    return json.dumps(data, indent=1)


@app.route('/getAllSudoUsers')
def get_all_sudo_users():
    data = u.getAllSudoUsers()
    return json.dumps(data, indent=1)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
