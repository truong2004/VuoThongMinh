//Include the library files
#include <LiquidCrystal_I2C.h>
#define BLYNK_PRINT Serial
#include <ESP8266WiFi.h>
#define BLYNK_TEMPLATE_ID "TMPL6r5t8Iwbo"
#define BLYNK_TEMPLATE_NAME "Hệ Thống Máy Bơm"
#define BLYNK_AUTH_TOKEN "9dZxjaXp51F9zC1jBf28BZfoij9usd8i"
#include <Blynk SimpleEsp8266.h>

//Initialize the LCD display
LiquidCrystal_I2C lcd(0x27, 16, 2);

char auth[] = "9dZxjaXp51F9zC1jBf28BZfoij9usd8i";  // Auth token
char ssid[] = "iPhone";                                // WIFI name
char pass[] = "12346789";                            // WIFI password

BlynkTimer timer;
bool Relay = 0;  // Biến điều khiển máy bơm

//Define component pins
#define sensor A0
#define waterPump D3

void setup() {
  Serial.begin(9600);
  pinMode(waterPump, OUTPUT);
  digitalWrite(waterPump, HIGH);  // Mặc định tắt máy bơm
  lcd.init();
  lcd.backlight();
 
  Blynk.begin(auth, ssid, pass, "blynk.cloud", 80);

  lcd.setCursor(1, 0);
  lcd.print("System Loading");
  for (int a = 0; a <= 15; a++) {
    lcd.setCursor(a, 1);
    lcd.print(".");
    delay(200);
  }
  lcd.clear();

  // Đo độ ẩm mỗi 2 giây
  timer.setInterval(2000L, soilMoistureSensor);
}

// Điều khiển máy bơm từ Blynk (nếu cần)
BLYNK_WRITE(V1) {
  Relay = param.asInt();  // Lấy giá trị từ nút trên Blynk

  if (Relay == 1) {  // Bật máy bơm thủ công
    digitalWrite(waterPump, LOW);
    lcd.setCursor(0, 1);
    lcd.print("Motor is ON ");
    Serial.println("Điều khiển từ Blynk: Bật máy bơm!");
  } else {  // Tắt máy bơm thủ công
    digitalWrite(waterPump, HIGH);
    lcd.setCursor(0, 1);
    lcd.print("Motor is OFF");
    Serial.println("Điều khiển từ Blynk: Tắt máy bơm!");
  }
}

// Đọc độ ẩm đất và điều khiển máy bơm tự động
void soilMoistureSensor() {
  int value = analogRead(sensor);
  value = map(value, 0, 1024, 0, 100);
  value = (value - 100) * -1;

  Blynk.virtualWrite(V0, value);  // Gửi giá trị độ ẩm lên Blynk
  lcd.setCursor(0, 0);
  lcd.print("Do am: ");
  lcd.print(value);
  lcd.print("%   ");  // Hiển thị giá trị độ ẩm với dấu %

  Serial.print("Giá trị analog đọc được: ");
  Serial.println(value);
  Serial.print("Độ ẩm: ");
  Serial.print(value);
  Serial.println("%");

  // Điều khiển máy bơm tự động dựa trên độ ẩm
  if (value < 50) {  // Nếu độ ẩm > 50%, tắt máy bơm
    Serial.println("Tự động: Tắt máy bơm!");
    digitalWrite(waterPump, HIGH);
    lcd.setCursor(0, 1);
    lcd.print("Motor is ON");
  } else {  // Nếu độ ẩm ≤ 50%, bật máy bơm
    Serial.println("Tự động: Bật máy bơm!");
    digitalWrite(waterPump, LOW);
    lcd.setCursor(0, 1);
    lcd.print("Motor is OFF ");
  }
}

void loop() {
  Blynk.run();   // Run the Blynk library
  timer.run();   // Run the Blynk timer
}