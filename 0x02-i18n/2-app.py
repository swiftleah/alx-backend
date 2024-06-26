#!/usr/bin/env python3
''' flask application code '''
from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    ''' determines best match for lanuages '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    ''' html file '''
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
