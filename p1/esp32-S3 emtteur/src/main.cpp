#include <Arduino.h>
#include <SPI.h>
#include <LoRa.h>

// Correspondance des broches selon cablage
#define LORA_SCK  12
#define LORA_MISO 13
#define LORA_MOSI 11
#define LORA_SS   10
#define LORA_RST  14
#define LORA_DIO0 9

// Fréquence (868 MHz)
#define BAND 868E6

int counter = 0;

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("--- Emetteur LoRa ESP32-S3 ---");

  // Initialisation du bus SPI avec les broches personnalisées de l'ESP32-S3
  SPI.begin(LORA_SCK, LORA_MISO, LORA_MOSI, LORA_SS);
  
  // Configuration des broches du module LoRa
  LoRa.setPins(LORA_SS, LORA_RST, LORA_DIO0);

  // Démarrage du module LoRa à 868 MHz
  if (!LoRa.begin(BAND)) {
    Serial.println("Erreur : Impossible d'initialiser le module LoRa. Verifie les branchements !");
    while (1);
  }

  // Optionnel : Configuration de la puissance d'émission (de 2 à 20 dBm)
  // LoRa.setTxPower(17);

  Serial.println("Module LoRa initialise avec succes !");
}

void loop() {
  Serial.print("Envoi du message : Ping ");
  Serial.println(counter);

  // Démarrage de l'envoi du paquet
  LoRa.beginPacket();
  LoRa.print("Ping ");
  LoRa.print(counter);
  LoRa.endPacket();

  counter++;
  
  // Attendre 2 secondes avant le prochain ping
  delay(2000);
}