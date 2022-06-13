from flask import flask

app = Flask(__name__)


@app.route('/')
def counter():
  reutrn 'Hello From Dylan'
