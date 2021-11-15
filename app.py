# Import flask
from flask import Flask

# Create an app
app = Flask(__name__)

# Define the index route
@app.route('/')
def hello_world():
    return 'Hello world'
    