import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def get_db():
    connection = sqlite3.connect("wagtopia.db")
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection

#home
@app.route("/")
def index():
    return render_template("index.html")

#parent
@app.route("/parent")
def parent():
    db = get_db()
    parents = db.execute("SELECT * FROM parents").fetchall()
    dogs = db.execute("SELECT * FROM dogs").fetchall()
    groomers = db.execute("SELECT * FROM groomers").fetchall()
    services = db.execute("SELECT * FROM services").fetchall()
    return render_template("parent.html", parents=parents, dogs=dogs, groomers=groomers, services=services)



if __name__ == "__main__":
    app.run(debug=True)
