#!/usr/bin/env python3
"""
Basic calendar front end.
"""

import datetime
from flask import Flask, render_template

from kalendar import Kalendar

app = Flask(__name__)  # pylint: disable=invalid-name


@app.route('/')
def main():
    """
    Return main page.
    """
    return 'Hello, World!'


@app.route('/cal')
def cal():
    """
    Retrun calendar view of all events
    """
    this_cal = Kalendar()
    this_cal.add_now("test1")
    this_cal.add_now("test2")

    to_display = ""
    for key, values in this_cal.get_all_elements().items():
        to_display += key + ":<BR>"
        for val in values:
            to_display += "&nbsp;&nbsp;&nbsp;&nbsp;" + val + "<BR>"

    return to_display


@app.route('/today')
def today():
    """
    Return activieties from today.
    """
    this_cal = Kalendar()
    this_cal.add_now("test1")
    this_cal.add_now("test2")
    return "<BR>".join(this_cal.get_all_elements(datetime.datetime.now()))


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    """
    Render greeting with name.
    """
    return render_template('hello.html', name=name)


if __name__ == "__main__":
    app.run(debug=True)
