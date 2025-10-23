from flask import Flask, render_template
from flask import jsonify
app = Flask(__name__)


from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Trang chủ
@app.route('/')
def index():
    return render_template("index.html")

# Trang giới thiệu
@app.route('/about')
def about():
    return render_template('about.html')
# Trang phản hồi
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Tạm thời in ra console (sau này có thể lưu DB)
        print(f"Phản hồi từ: {name} - {email}")
        print(f"Nội dung: {message}")

        return render_template('thankyou.html', name=name)
    return render_template('feedback.html')
# API cung cấp dữ liệu cảm biến
@app.route('/api/sensors')
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
