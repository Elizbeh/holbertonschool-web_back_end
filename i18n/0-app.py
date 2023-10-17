#!/usr/bin/env python3
"""
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():

    return render_template('0-index.html')

