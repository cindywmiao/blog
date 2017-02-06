# -*- coding: utf-8 -*-

import re
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/demo')
def demo():
    return render_template('demo.html')


if __name__ == '__main__':
    app.run()
