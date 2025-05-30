# import sqlite3


from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/lore")
def start():
    return render_template("index.html")
@app.route("/weapon")
def start1():
    return render_template("index1.html")
app.run()