 Vườn Thông Minh Ứng Dụng AI và IoT

📌 Giới Thiệu

Hệ thống vườn thông minh là một giải pháp ứng dụng IoT và trí tuệ nhân tạo (AI) nhằm giám sát và điều khiển tự động môi trường vườn. Hệ thống giúp theo dõi tình trạng đất, ánh sáng, độ ẩm, tự động tưới nước và nhận diện hình ảnh để phát hiện người lạ xâm nhập hoặc xác định thời điểm thu hoạch cây trồng.

🎯 Mục Tiêu

- Xây dựng hệ thống IoT thu thập dữ liệu từ môi trường.
- Triển khai AI phân tích hình ảnh và tối ưu hoá việc chăm sóc cây trồng.
- Phát triển giao diện web trực quan để giám sát và điều khiển từ xa.
- Ứng dụng nhận diện hình ảnh để phát hiện người lạ và gửi cảnh báo qua Telegram.

 🏢 Kiến Trúc Hệ Thống
1. Phần Cứng
- Cảm biến: Độ ẩm đất, ánh sáng, cảm biến mưa.
- Thiết bị điều khiển: Arduino Uno, ESP32/ESP8266.
- Thiết bị tự động: Máy bơm nước, relay, màn hình LCD.
- Camera: ESP32-CAM phục vụ nhận diện hình ảnh.

2. Phần Mềm
- Giám sát môi trường: Hiển thị dữ liệu cảm biến theo thời gian thực.
- Tưới cây tự động:
  - Khi độ ẩm đất < 50% → Bật máy bơm.
  - Khi độ ẩm đất > 50% → Tắt máy bơm.
- Nhận diện người lạ: Gửi cảnh báo khi phát hiện người lạ xâm nhập.
- Nhận diện cây trồng: Phân tích hình ảnh để xác định rau đã đến thời điểm thu hoạch.

🚀 Hướng Dẫn Cài Đặt

1. Yêu cầu hệ thống
- Phần mềm: Python 3.13.2, Arduino IDE.
- Thư viện: ESP32, ESP8266, OpenCV, Flask, YOLOv8.

2. Cài đặt

# Clone repository
git clone git@github.com:your-repo-url.git
cd VuonThongMinh

# Cài đặt thư viện Python
pip install ultralytics opencv-python torch torchvision numpy

# Chạy server
python app.py


3. Kết nối phần cứng
- Nạp code vào Arduino/ESP32.
- Kiểm tra các cảm biến hoạt động đúng.

📊 Giao Diện Web
- Hiển thị dữ liệu cảm biến dưới dạng biểu đồ.
- Bật/tắt bơm nước từ xa.
- Hiển thị cảnh báo khi phát hiện người qua Telegram.

🤖 AI và Nhận Diện Hình Ảnh
- Mô hình: Dùng YOLOv8 nhận diện người lạ và phân tích rau.
- Xử lý ảnh: Dùng **OpenCV** trích xuất thông tin.
- Lưu trữ log: Ghi nhận hình ảnh khi phát hiện người.

📝 Nhóm Thực Hiện
- Thành viên: Đỗ Ngọc Nghĩa, Bùi Văn Trường, Nguyễn Thành Hưng, Nguyễn Chí Nhật.
- Lớp: CNTT 16-03.

🚀 Hệ thống vườn thông minh - Tối ưu hoá nông nghiệp với AI và IoT!

