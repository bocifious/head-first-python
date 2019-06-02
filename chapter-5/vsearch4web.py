# production program for web search app

# import Flask class from the flask module
# import search4letters class from the vsearch module (chapter 4)
from flask import Flask, render_template
from vsearch import search4letters

# create an object type of Flask assigning it to app variable
app = Flask(__name__)

# function decorator and function
@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'


# add new route for search4 and then function to search
# for set within phrase by using imported module search4letters
@app.route('/search4')
def do_search() -> str:
    return str(search4letters('life, the universe, and everything', 'eiru,!'))


# function to return rendered HTML
@app.route('/entry')
def entry_page() -> 'html':
    return render_template(
        'entry.html', the_title='Welcome to search4letters on the web!'
    )


# used to run the webapp 'app' in the web server
app.run()
