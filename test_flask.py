import os
from flask import Flask, render_template

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'images')

@app.route("/")
def home():
    return render_template("static/templates/index.html")