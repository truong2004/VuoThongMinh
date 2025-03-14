import cv2
import numpy as np
from flask import Flask, Response, render_template
from ultralytics import YOLO
import requests
import datetime

app = Flask(__name__)

ESP32_IP = "http:/172.16.18.79:81/stream"  # Thay bằng IP thực tế của ESP32-CAM
YOLO_MODEL = "yolov8n-seg.pt"  # Model segmentation
TELEGRAM_BOT_TOKEN = "7565316426:AAGcX35IaebMd5O4rRPsf3355ExqLbYxIDg"
TELEGRAM_CHAT_ID = "7077556124"

# Load mô hình YOLOv8 segmentation
model = YOLO(YOLO_MODEL)

# Gửi cảnh báo qua Telegram
def send_alert(image):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    _, img_encoded = cv2.imencode(".jpg", image)
    files = {"photo": ("alert.jpg", img_encoded.tobytes())}
    data = {"chat_id": TELEGRAM_CHAT_ID, "caption": f"🚨 Cảnh báo: Phát hiện người lúc {timestamp}"}
    requests.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto", data=data, files=files)

# Nhận diện đối tượng bằng segmentation
def detect_objects(frame):
    results = model(frame)
    person_detected = False  

    for result in results:
        if result.masks:  
            for box, mask in zip(result.boxes, result.masks.xy):
                conf = box.conf[0].item()
                cls = int(box.cls[0])  
                
                if conf < 0.5:
                    continue
                
                mask = np.array(mask, np.int32)
                label = "Unknown"

                # Phân loại màu sắc theo nhóm
                COLORS = {
                    "nguoi": (255, 0, 0),       # Người - Đỏ
                    "dat": (139, 69, 19),       # Đất - Nâu đất
                    "dat_xam": (105, 105, 105), # Đất - Xám
                    "rau_nho": (34, 139, 34),   # Rau nhỏ - Xanh lá cây đậm
                    "rau_lon": (0, 255, 127)    # Rau lớn - Xanh lá sáng
                }

                # Xác định diện tích mask để phân biệt rau thu hoạch và chưa thu hoạch
                area = cv2.contourArea(mask)

                if cls == 0:  # Người
                    label = "Người"
                    color = COLORS["nguoi"]
                    person_detected = True  
                elif cls == 1:  # Đất trống (nâu và xám)
                    label = "Đất"
                    color = COLORS["dat"] if np.random.rand() > 0.5 else COLORS["dat_xam"]
                elif cls == 2 or cls == 3:  # Rau (dùng diện tích để xác định)
                    if area < 5000:  # Giới hạn diện tích (có thể điều chỉnh)
                        label = "Rau nhỏ"
                        color = COLORS["rau_nho"]
                    else:
                        label = "Rau lớn"
                        color = COLORS["rau_lon"]

                # Vẽ contour thay vì hình chữ nhật
                cv2.polylines(frame, [mask], isClosed=True, color=color, thickness=3)
                cv2.putText(frame, label, (mask[0][0], mask[0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    # Gửi cảnh báo nếu phát hiện người
    if person_detected:
        send_alert(frame)

    return frame

# Kết nối ESP32-CAM
def connect_camera():
    cap = cv2.VideoCapture(ESP32_IP)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    return cap

# Xử lý stream video
def generate_frames():
    cap = connect_camera()
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        frame = detect_objects(frame)
        _, buffer = cv2.imencode(".jpg", frame)
        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + buffer.tobytes() + b"\r\n")
    cap.release()

# Giao diện web
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/video_feed")
def video_feed():
    return Response(generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")

# Chạy ứng dụng Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)