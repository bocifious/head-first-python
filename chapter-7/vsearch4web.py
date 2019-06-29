# production program for web search app

# import Flask, render_template, and request classes from the flask module
# import search4letters class from the vsearch module (chapter 4)
from flask import Flask, render_template, request, escape
from vsearch import search4letters
import mysql.connector

# create an object type of Flask assigning it to app variable
app = Flask(__name__)

#function to log requests to mysql database
def log_request(req: 'flask_request', res: str) -> None:
    """function to log results of search4letters function"""
    dbconfig = {'host': '127.0.0.1',
                'user': 'vsearch',
                'password': 'vsearchpasswd',
                'database': 'vsearchlogDB', }
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """insert into log
              (phrase, letters, ip, browser_string, results)
              values
              (%s, %s, %s, %s, %s)"""
    cursor.execute(_SQL,    (req.form['phrase'],
                            req.form['letters'],
                            req.remote_addr,
                            req.user_agent.browser,
                            res, ))
    conn.commit()
    cursor.close()
    conn.close()

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
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                            the_title='View Log',
                            the_row_titles=titles,
                            the_data=contents,)


# used to run the webapp 'app' in the web server
if __name__ == '__main__':
    app.run(debug=True)
