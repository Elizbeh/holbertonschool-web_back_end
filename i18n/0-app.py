#!/usr/bin/env python3
"""Setup a basic Flask app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    """A basic Flask app that creates
    a single / and an html template
    """
    return render_template('0-index.html')
