import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "air_quality_model.pkl")

def train_model():
    """Huấn luyện mô hình dự đoán chất lượng không khí"""
    # Dữ liệu mẫu: giả lập (nhiệt độ, độ ẩm, áp suất, chỉ số AQI)
    data = {
        "temperature": [25, 28, 30, 32, 35, 22, 24, 26, 29, 33],
        "humidity": [60, 55, 50, 48, 40, 70, 65, 68, 52, 45],
        "pressure": [1012, 1010, 1008, 1005, 1003, 1015, 1013, 1011, 1007, 1006],
        "aqi": [50, 60, 70, 80, 100, 40, 45, 55, 75, 90]
    }

    df = pd.DataFrame(data)

    X = df[["temperature", "humidity", "pressure"]]
    y = df["aqi"]

    model = LinearRegression()
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
    print("✅ Mô hình đã được huấn luyện và lưu vào:", MODEL_PATH)


def predict_air_quality(temp, hum, pres):
    """Dự đoán AQI dựa trên dữ liệu cảm biến"""
    if not os.path.exists(MODEL_PATH):
        train_model()  # Nếu chưa có model, tự động huấn luyện

    model = joblib.load(MODEL_PATH)
    X_new = np.array([[temp, hum, pres]])
    prediction = model.predict(X_new)[0]

    # Xếp loại dựa vào mức AQI
    if prediction < 50:
        level = "Tốt"
    elif prediction < 100:
        level = "Trung bình"
    else:
        level = "Ô nhiễm"

    return {
        "aqi": round(prediction, 2),
        "level": level
    }


# ✅ Kiểm tra nhanh khi chạy riêng file này
if __name__ == "__main__":
    train_model()
    result = predict_air_quality(30, 55, 1009)
    print("Kết quả dự đoán:", result)
