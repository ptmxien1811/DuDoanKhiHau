import pyodbc

def get_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=AirQualityDB;"
        "UID=sa;"
        "PWD=123456;"  # thay bằng mật khẩu thật của bạn
    )
    return conn
