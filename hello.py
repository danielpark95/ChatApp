from flask import Flask

# __name__ refers to name of current python module
# App instance handles incoming web requests and sends responses to user
app = Flask(__name__)

# Decorator that turns a regular python function into a Flask view function
# converts function's return value into http response to be displayed by web browser.
# Pass '/' to signify web requests with main URL '/'
@app.route('/')
def hello():
    return "Hello, world"




