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
    this_cal = Kalendar()
    this_cal.add_now("test1")
    this_cal.add_now("test2")

    this_cal.add_element(
        "test 3",
        datetime.datetime.strptime("22/11/19 18:00", "%d/%m/%y %H:%M")
    )

    this_cal.add_element(
        "old_test",
        datetime.datetime.strptime("21/11/06 12:00", "%d/%m/%y %H:%M")
    )
    this_cal.add_element(
        "another old object",
        datetime.datetime.strptime("01/01/19 01:00", "%d/%m/%y %H:%M")
    )

    return 'Hello, World!'


@app.route('/cal')
def cal():
    """
    Retrun calendar view of all events
    """
    this_cal = Kalendar()
    to_display = ""

    for elements in this_cal.get_all_elements():
        to_display += elements["key"] + ":<BR>"
        for element in elements["value"]:
            to_display += "&nbsp;&nbsp;&nbsp;&nbsp;" + str(element) + "<BR>"

    return to_display


@app.route('/today')
def today():
    """
    Return activieties from today.
    """
    this_cal = Kalendar()
    to_display = "TODAY:<BR><BR>"

    elements = this_cal.get_all_day_elements(datetime.datetime.now())
    for element in elements:
        for key, values in element.items():
            to_display += key + ":<BR>"
            for val in values:
                to_display += "&nbsp;&nbsp;&nbsp;&nbsp;" + val + "<BR>"

    return to_display


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    """
    Render greeting with name.
    """
    return render_template('hello.html', name=name)


if __name__ == "__main__":
    app.run(debug=True)
