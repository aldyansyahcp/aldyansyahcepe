from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def ok():
    return render_template("index.html")
