from curses import flash
from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/getachievements/', methods=['GET'])
def get():
    print(request.args)
    return "ok"