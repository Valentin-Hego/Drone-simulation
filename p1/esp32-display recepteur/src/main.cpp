#include <Arduino.h>
#include <SPI.h>
#include <LoRa.h>
#include <TFT_eSPI.h>

// Broches LoRa pour le LilyGO T-Display V1.1
#define LORA_SCK  21
#define LORA_MISO 17
#define LORA_MOSI 22
#define LORA_SS   15
#define LORA_RST  12
#define LORA_DIO0 26

#define BAND 868E6

// Instance de l'écran TFT
TFT_eSPI tft = TFT_eSPI();

void setup() {
  Serial.begin(115200);
  delay(1000);

  // Allumer le rétroéclairage de l'écran
  pinMode(TFT_BL, OUTPUT);
  digitalWrite(TFT_BL, HIGH);

  // Initialisation de l'écran
  tft.init();
  tft.setRotation(1); // Mode paysage (horizontal)
  tft.fillScreen(TFT_BLACK);
  tft.setTextColor(TFT_WHITE, TFT_BLACK);
  tft.setTextSize(2);

  tft.setCursor(10, 10);
  tft.println("Recepteur LoRa");
  tft.setCursor(10, 45);
  tft.println("En attente...");

  // Initialisation du bus SPI pour le LoRa
  SPI.begin(LORA_SCK, LORA_MISO, LORA_MOSI, LORA_SS);
  LoRa.setPins(LORA_SS, LORA_RST, LORA_DIO0);

  // Démarrage de la radio LoRa
  if (!LoRa.begin(BAND)) {
    tft.fillScreen(TFT_RED);
    tft.setCursor(10, 50);
    tft.println("Erreur LoRa !");
    while (1);
  }
}

void loop() {
  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    String message = "";
    while (LoRa.available()) {
      message += (char)LoRa.read();
    }
    int rssi = LoRa.packetRssi();

    // Effacer la zone d'affichage dynamique pour éviter la superposition du texte
    tft.fillRect(10, 45, 220, 80, TFT_BLACK);

    // Afficher le message reçu
    tft.setCursor(10, 45);
    tft.print("Msg: ");
    tft.println(message);

    // Afficher la puissance du signal RSSI
    tft.setCursor(10, 75);
    tft.print("RSSI: ");
    tft.print(rssi);
    tft.println(" dBm");
  }
}