#!/bin/env python
# -*- coding: utf-8 -*-

import bbbroom.bbbclient

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('start.html')

@app.route('/join')
def join():
    return render_template('join.html')


@app.route('/join_meeting')
def repofile():
    bbbroom.bbbclient.join_room()
    return ''


if __name__ == "__main__":
    app.run(debug=True)
