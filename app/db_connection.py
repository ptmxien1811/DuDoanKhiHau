import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        # Thông tin kết nối
        connection = mysql.connector.connect(
            host='localhost',        # hoặc '127.0.0.1'
            user='root',             # tên người dùng MySQL
            password='Ntnn1009@',    # mật khẩu MySQL (chú ý viết đúng biến là password)
            database='demo',         # tên cơ sở dữ liệu
            port=3306                # cổng mặc định của MySQL
        )

        # Kiểm tra kết nối
        if connection.is_connected():
            print("✅ Kết nối MySQL thành công!")
            db_info = connection.get_server_info()
            print("Phiên bản MySQL:", db_info)

            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print("Đang sử dụng cơ sở dữ liệu:", record)

    except Error as e:
        print("❌ Lỗi khi kết nối MySQL:", e)

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("🔒 Đã đóng kết nối MySQL.")

# Gọi hàm
if __name__ == "__main__":
    connect_to_mysql()
