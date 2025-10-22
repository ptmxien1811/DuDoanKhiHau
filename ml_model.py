import pandas as pd
from sklearn.linear_model import LinearRegression
from db_connection import get_connection

def train_and_predict():
    conn = get_connection()
    query = "SELECT * FROM SensorData"
    df = pd.read_sql(query, conn)

    X = df[['Temperature', 'Humidity']]
    y_air = df['PM25']
    y_noise = df['NoiseLevel']

    model_air = LinearRegression().fit(X, y_air)
    model_noise = LinearRegression().fit(X, y_noise)

    new_data = pd.DataFrame({
        'Temperature': [30],
        'Humidity': [70]
    })
    air_pred = model_air.predict(new_data)[0]
    noise_pred = model_noise.predict(new_data)[0]

    print(f"Dự đoán: PM2.5={air_pred:.2f}, Noise={noise_pred:.2f} dB")
    return air_pred, noise_pred
