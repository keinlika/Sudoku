# ESP8266 NodeMCU – Blynk IoT LED Control Lab

## Overview
This project uses the ESP8266 NodeMCU and the Blynk IoT (Blue) platform to remotely
control the onboard LED using a Button widget through Virtual Pin **V0**.

## Blynk Template
- **Template ID:** TMPL2qmrNp1IY  
- **Template Name:** Quickstart Template

## WiFi Configuration
- **SSID:** UC_Wifi_2  
- **Password:** ucourtyard

## Description
The NodeMCU connects to Wi-Fi and the Blynk Cloud using the device’s Auth Token.
A button widget (V0) on the Blynk dashboard sends values (1 = ON, 0 = OFF).  
The firmware listens to V0 via `BLYNK_WRITE(V0)` and toggles the onboard LED (GPIO16).

## How to Use
1. Open the `.ino` file in Arduino IDE.
2. Install ESP8266 and Blynk libraries.
3. Insert your Blynk **AUTH TOKEN**.
4. Select board: *NodeMCU 1.0 (ESP-12E Module)*.
5. Upload the sketch.
6. Use the Blynk dashboard button to toggle the LED.

## Results
The LED toggles correctly from the Blynk dashboard, confirming
successful Wi-Fi and cloud communication.

## Files Included
- `NodeMCU_Blynk_LED.ino`
- `README.md`
