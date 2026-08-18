#include <Arduino.h>
#include <stdint.h>
#include <TFT_eSPI.h>

#define MAX_BUFF_LEN 255

TFT_eSPI tft = TFT_eSPI();
char c;
char str[MAX_BUFF_LEN];
uint8_t idx = 0;

void setup()
{
    Serial.begin(115200);
    tft.begin();
    tft.setRotation(1);
    tft.fillScreen(TFT_BLACK);
    tft.setCursor(100,65);
    tft.setTextColor(TFT_GREEN, TFT_BLACK);
    tft.setTextSize(3); 
}

void loop()
{
    if (Serial.available() > 0) {
        c = Serial.read();

        if (c != '\n' && c != '\r') {
            if (idx < MAX_BUFF_LEN - 1) {
                str[idx++] = c;
            }
        }
        else if (c == '\n') {
            tft.fillScreen(TFT_BLACK);
            tft.setCursor(100,65);
            str[idx] = '\0';
            idx = 0;
            tft.println(str);
        }
    }
}