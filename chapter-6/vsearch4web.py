# production program for web search app

# import Flask, render_template, and request classes from the flask module
# import search4letters class from the vsearch module (chapter 4)
from flask import Flask, render_template, request
from vsearch import search4letters

# create an object type of Flask assigning it to app variable
app = Flask(__name__)

def log_request(req: 'flask_request', res: str) -> None:
    """function to log results of search4letters function"""
    with open('vsearch.log', 'a') as log:
        print(req, res, file=log)

# add new route for search4 and then function to search
# for set within phrase by using imported module search4letters
@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results: '
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template(
        'results.html', the_phrase=phrase,
        the_letters=letters, the_title=title,
        the_results=results
    )


# function to return rendered HTML
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template(
        'entry.html', the_title='Welcome to search4letters on the web!'
    )


@app.route('/viewlog')
def view_the_log() -> str:
    with open('vsearch.log') as log:
        contents = log.read()
    return contents

# used to run the webapp 'app' in the web server
if __name__ == '__main__':
    app.run(debug=True)
