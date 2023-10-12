import base64
from http.client import OK
import io
import os
from flask import Flask, jsonify, send_file, render_template, request

# Importing Required Modules
from rembg import remove
from PIL import Image

app = Flask(__name__)
app.config["UPLOAD"] = "."


@app.route("/")
def home():
    return render_template("./home.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["img"]
    filename = file.filename + ".png"
    input = Image.open(file)
    output = remove(input)
    output.save(filename, format="png")

    return send_file(filename, mimetype="image/png")


@app.route("/", methods=["delete"])
def delete_file():
    filename = request.args.get("fileName")
    if os.path.isfile(filename):
        os.remove(filename)
    return "ok"
