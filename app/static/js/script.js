function loadData() {
    const result = document.getElementById("result");
    result.textContent = "Đang tải dữ liệu...";

    // Giả lập dữ liệu
    setTimeout(() => {
        result.textContent = "Dự đoán: Nhiệt độ trung bình 27°C, độ ẩm 68%";
    }, 1500);
}