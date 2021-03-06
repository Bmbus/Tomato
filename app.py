from flask import Flask, render_template, jsonify, redirect, url_for
from src.dataminer import Dataminer
from core import Database, error

app = Flask(__name__)
db = Database()
dm = Dataminer()

with open("README.md", "r") as rm:
    readme = rm.read()

@app.route("/login")
def login():
    return render_template("login.html", title="Tomato | Login")

@app.route("/")
def index():
    return render_template("index.html", hum=dm.get_h_t()["humidity"], temp=dm.get_h_t()["temperature"], title="Tomato - Home", username="Jannes") # TODO get username from Database

@app.route("/graphics")
def graphics():
    return render_template("graphics.html", title="Tomato - Graphics")

@app.route("/config")
def config():
    return render_template("config.html", title="Tomato - Config")

@app.route("/raw_data")
def raw_data():
    return render_template("raw_data.html", title="Tomato - RawData")

@app.route("/log")
def logging():
    return render_template("log.html", title="Tomato - Log", log=dm.read_csv())

@app.route("/about")
def about():
    return render_template("about.html", title="Tomato - About", readme=readme)

@app.route("/init")
def init():
    db.setup()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.register_blueprint(error)
    try:
        db.setup()
        app.run(debug=True, port=8080, threaded=True, host="0.0.0.0")
    except:
        app.run(debug=True, port=8080, threaded=True, host="0.0.0.0")