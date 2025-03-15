# 🌱 Vườn Thông Minh Ứng Dụng AI & IoT

## 📌 Giới Thiệu
Hệ thống vườn thông minh là một giải pháp kết hợp IoT và trí tuệ nhân tạo (AI) để giám sát và điều khiển tự động môi trường vườn. Hệ thống giúp:

✅ Theo dõi tình trạng đất, ánh sáng, độ ẩm.
✅ Tưới nước tự động.
✅ Nhận diện hình ảnh để phát hiện người lạ xâm nhập.
✅ Xác định thời điểm thu hoạch cây trồng.

---
## 🎯 Mục Tiêu
- 📡 Xây dựng hệ thống IoT thu thập dữ liệu môi trường.
- 🧠 Triển khai AI phân tích hình ảnh, tối ưu hóa việc chăm sóc cây trồng.
- 📱 Phát triển giao diện app Blynk trực quan để giám sát & điều khiển từ xa.
- 🚨 Nhận diện người lạ và gửi cảnh báo qua Telegram.

---
## 🏢 Kiến Trúc Hệ Thống

### 1️⃣ Phần Cứng
- Cảm biến: Độ ẩm đất, ánh sáng, cảm biến mưa.
- Thiết bị điều khiển: Arduino Uno, ESP32/ESP8266.
- Thiết bị tự động: Máy bơm nước, relay, màn hình LCD.
- Camera: ESP32-CAM phục vụ nhận diện hình ảnh.

### 2️⃣ Phần Mềm
- 📊 Giám sát môi trường: Hiển thị dữ liệu cảm biến thời gian thực.
- 💧 Tưới cây tự động:
  - Khi Độ ẩm đất < 50% → Bật máy bơm.
  - Khi độ ẩm đất > 50% → Tắt máy bơm.
- 🌍 Điều khiển từ xa: Bật/tắt thiết bị qua app Blynk.
- 🔍 Nhận diện người lạ: Gửi cảnh báo khi phát hiện xâm nhập.
- 🌿 Nhận diện cây trồng: Phân tích hình ảnh để xác định thời điểm thu hoạch.

---
## 🚀 Hướng Dẫn Cài Đặt

### 1️⃣ Yêu Cầu Hệ Thống
- Phần mềm: Python 3.13.2, Arduino IDE.
- Thư viện: ESP32, ESP8266, Blynk, OpenCV, Flask.

### 2️⃣ Cài Đặt

# Clone repository
git clone https://github.com/Nghia2624/VuonThongMinh
cd VuonThongMinh

# Cài đặt thư viện Python
pip install opencv-python numpy flask ultralytics requests

# Chạy server
python app.py


### 3️⃣ Kết Nối Phần Cứng
- Nạp code vào Arduino/ESP32.
- Kiểm tra cảm biến hoạt động đúng.
- Kết nối ESP32-CAM để lấy link.

---
## 📊 Giao Diện Web
- 📷 Hiển thị hình ảnh trực tiếp từ camera ESP32.
- 🔔 Phát cảnh báo** về điện thoại khi phát hiện người lạ qua Telegram.

---
## 🤖 AI & Nhận Diện Hình Ảnh
- 🏆 Mô hình: Dùng YOLOv8 để nhận diện người lạ & cây trồng.
- 🖼️ Xử lý ảnh: Dùng OpenCV trích xuất thông tin.
- 📜 Lưu trữ log: Ghi nhận hình ảnh khi phát hiện người xâm nhập.

---
## 📝 Nhóm Thực Hiện
- 👨‍💻 Thành viên: Đỗ Ngọc Nghĩa, Bùi Văn Trường, Nguyễn Thành Hưng, Nguyễn Chí Nhật.
- 🏫 Lớp: CNTT 16-03.

🚀 Hệ thống vườn thông minh - Tối ưu hoá nông nghiệp với AI & IoT! 🌾
## Hình ảnh thực tế 
![mohinh](https://github.com/user-attachments/assets/2b13e464-cbc9-4e0c-93fa-93888907f599)


