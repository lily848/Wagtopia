import sqlite3
from flask import Flask, render_template, request, jsonify

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

ALL_TIMES = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"]
@app.route("/available-times")
def available_times():
    groomer_id = request.args.get("groomer_id")
    date = request.args.get("date")
    db = get_db()
    taken_times = db.execute(
        "SELECT start_time FROM bookings WHERE groomer_id = ? AND appointment_date = ?",(groomer_id,date)
    ).fetchall()
    availible = [t for t in ALL_TIMES if t not in taken_times]
    return jsonify({"availible" : availible})

if __name__ == "__main__":
    app.run(debug=True)
