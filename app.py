# Import dependencies
from flask import Flask

# Creates a new Flask app instance
app = Flask(__name__)

# Define the root (/) as the starting point and create a function
@app.route('/')
def hello_world():
    return 'Hello world'

    