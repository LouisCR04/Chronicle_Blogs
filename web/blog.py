#!/usr/bin/env python3
"""
Main Flask Router
"""
from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Ichibe Hyosube',
        'title': 'Zanpakuto',
        'content': 'First Zanpakuto',
        'date_posted': 'January 1, 2020'
    },
    {
        'author': 'Aizen Souske',
        'title': 'Hogyoku',
        'content': 'First Hogyoku',
        'date_posted': 'January 14, 2021'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title='About Seiretei')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
