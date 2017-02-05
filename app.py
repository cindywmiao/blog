# -*- coding: utf-8 -*-

import re
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route('/_calculate')
def calculate():
    return jsonify(result='I Catch a BUG!')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
