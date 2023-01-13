from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'kubectl is running successfully from jenkins!!!'
