# My Hackpad Project

## Overview

This project is a custom hackpad designed to control macros and multimedia functions with a small, 2×3 key layout. It features an OLED display, EC11 rotary encoder, and supports programmable macros via KMK firmware.

---

## Overall Layout and Usage

The hackpad features a compact layout with:
- **6 programmable keys** arranged in a 2×3 grid
- **EC11 rotary encoder** with push-button for volume control and mute functionality
- **OLED display** (128×32, SSD1306) for displaying layer information and status
- **RP2040 microcontroller** running KMK firmware for macro programming
- **Custom 3D-printed case** with professional design aesthetics

---

## Schematic

The schematic shows how all the components are connected, including rows/columns for the keys, the OLED display, and the rotary encoder.

![Schematic](https://i.imgur.com/3TPDfmo.png)

---

## PCB

A screenshot of the PCB layout with component placement annotations.

![PCB Layout](https://i.imgur.com/Y9XwnsQ.png)
![PCB Layout](https://i.imgur.com/UBnd58N.png)

---

## Case

The custom case demonstrates how the PCB and components fit together. This design features mounting points for the RP2040, rotary encoder, and OLED display.

![Case Design](https://i.imgur.com/b3M2yuL.png)

---

## Bill of Materials (BOM)

| Part | Quantity | Notes |
|------|----------|-------|
| Microcontroller (RP2040) | 1 | Main controller |
| Switches | 6 | For the 2×3 layout |
| Diodes (1N4148) | 6 | For key matrix |
| EC11 Rotary Encoder | 1 | With push button |
| OLED Display (SSD1306, 128×32) | 1 | I2C interface |
| Resistors | As needed | For encoder pull-ups and pull-downs |
| Capacitors | As needed | Decoupling and filtering |
| PCB | 1 | Custom design (KiCad) |
| Case | 1 | 3D printed |

---


## Notes 
Hello! i really enjoyed this project, even when i was very scared to do everything right. and make no mistakes. this took me like 4 days to complete. please tell me if anything is wrong and ill fix it ASAP. the firmware is not full because i never done hw and dont know much about how it works. THANKS!
---
