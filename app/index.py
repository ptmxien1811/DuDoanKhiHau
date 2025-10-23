from flask import Flask, render_template
from flask import jsonify
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
@app.route('/about')
def about():
    return render_template('about.html')
def api_sensors():
    data = [
        {"id": 1, "name": "Cảm biến 1", "location": "Quận 1", "pm25": 45, "noise": 62, "timestamp": "2025-10-23 10:00",
         "image": "sensor1.jpg"},
        {"id": 2, "name": "Cảm biến 2", "location": "Quận 3", "pm25": 80, "noise": 70, "timestamp": "2025-10-23 10:05",
         "image": "sensor2.jpg"},
        {"id": 3, "name": "Cảm biến 3", "location": "Bình Thạnh", "pm25": 29, "noise": 55,
         "timestamp": "2025-10-23 10:10", "image": "sensor3.jpg"},
    ]
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)