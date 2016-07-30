# -*- coding:utf-8 -*-

import os

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('build/en/index.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
