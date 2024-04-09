#!/usr/bin/env python3
''' basic flask application code '''
from Flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() - > str:
    ''' renders basic html template '''
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
