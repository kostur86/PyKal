from flask import Flask, render_template
import datetime

from kalendar import Kalendar

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/cal')
def cal():
    cal = Kalendar()
    cal.addNow("test1")
    cal.addNow("test2")

    toDisplay = ""
    for key, values in cal.getAllElements().items():
        toDisplay += key + ":<BR>"
        for val in values:
            toDisplay += "&nbsp;&nbsp;&nbsp;&nbsp;" + val + "<BR>"

    return toDisplay


@app.route('/today')
def today():
    cal = Kalendar()
    cal.addNow("test1")
    cal.addNow("test2")
    return "<BR>".join(cal.getAllElements(datetime.datetime.now()))

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
