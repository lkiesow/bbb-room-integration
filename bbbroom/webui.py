#!/bin/env python
# -*- coding: utf-8 -*-

import bbbroom.bbbclient

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/whiteboard')
def repofile():
    bbbroom.bbbclient.whiteboard()
    return ''


if __name__ == "__main__":
    app.run(debug=True)
