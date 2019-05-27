# introduction to flask web apps

# import Flask class from the flask module
from flask import Flask

# create an object type of Flask assigning it to app variable
app = Flask(__name__)

# function decorator and function
@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'


# used to run the webapp 'app' in the web server
app.run()
