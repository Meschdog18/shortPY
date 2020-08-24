from flask import Flask, redirect, render_template, request
from validator_collection import checkers

from module.controller import Controller

app = Flask(__name__)


@app.route('/<myid>')
def hello(myid):
    url = Controller().db_get(myid)
    return redirect(url, code=302)
@app.route('/')
def index():
    return render_template('add_url.html')
@app.route('/', methods=['POST'])
def index_post():
    text = request.form['text']
    if checkers.is_url(text):
        key = Controller().db_insert(text)
        if key:
            return 'Your new url is http://127.0.0.1:5000/'+key
        else:
            return 'Error'
    else:
        return 'Error: Must be a valid url'
if __name__ == '__main__':
    

    app.run()


