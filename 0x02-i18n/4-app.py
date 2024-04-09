#!/usr/bin/env python3
""" Flask application code """
from typing import Union
from flask import Flask, request
from flask_babel import Babel
from config import Config
from routes.routes_4 import app_routes


app = Flask(__name__)
babel = Babel(app)

app.config.from_object(Config)
app.register_blueprint(app_routes)


@babel.localeselector
def get_locale() -> Union[str, None]:
    """ get language """
    localeReq = request.args.get('locale')
    if localeReq and locale in Config.LANGUAGES:
        return localeReq
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
