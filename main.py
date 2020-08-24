from flask import Flask, redirect

from module.controller import Controller

app = Flask(__name__)


@app.route('/<myid>')
def hello(myid):
    url = Controller().db_get(myid)
    return redirect(url, code=302)
@app.route('/')
def gi():
    return 'helo'
if __name__ == '__main__':
    

    app.run()


