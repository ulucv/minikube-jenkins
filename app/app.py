from flask import Flask, render_template, request, jsonify
import pytz
from datetime import datetime

app = Flask(__name__)

CITIES = {
    "Istanbul": "Europe/Istanbul",
    "Amsterdam": "Europe/Amsterdam",
    "London": "Europe/London",
    "Sydney": "Australia/Sydney",
    "Mumbai": "Asia/Kolkata",
    "Beijing": "Asia/Shanghai",
    "New York": "America/New_York",
    "Los Angeles": "America/Los_Angeles"
}

selected_cities = []

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", cities=CITIES.keys(), selected_cities=selected_cities)

@app.route("/add_city", methods=["POST"])
def add_city():
    data = request.get_json()
    city = data.get("city")
    if city in CITIES and city not in selected_cities:
        selected_cities.append(city)
    return jsonify({"success": True})

@app.route("/remove_city", methods=["POST"])
def remove_city():
    data = request.get_json()
    city = data.get("city")
    if city in selected_cities:
        selected_cities.remove(city)
    return jsonify({"success": True})

@app.route("/get_time")
def get_time():
    city = request.args.get("city")
    if city in CITIES:
        current_time = datetime.now(pytz.timezone(CITIES[city])).strftime("%Y-%m-%d %H:%M:%S")
        return jsonify({"time": current_time})
    return jsonify({"error": "Invalid city"}), 400

if __name__ == "__main__":
    app.run(debug=True)
