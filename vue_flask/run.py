""" Runs flask web server for demo app.

Use one of the following commands to run the application:

    `$ python run.py`
    or
    `$ python -m flask run`
"""

import os
from flask import Flask, current_app, send_file

app = Flask(__name__, static_folder="dist/static", static_url_path="/static")


@app.route("/", defaults={'path': ""})
@app.route("/<path:path>")
def index_client(path):
    if path == "favicon.ico":
        return ""
    if path == "":
        path = "index.html"
    entry = os.path.join("dist/", path)
    return send_file(entry)


app.run(port=5000)
