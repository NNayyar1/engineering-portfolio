# Arduino Droplet Detector (Photodiode + LED)

An arduino project that detects water droplets using an LED and photoresistor pair. Includes PWM control, sensor calibration, real-time monitoring, and CSV logging.

## Overview
This project uses a photodiode to detect changes in light caused by water droplets interrupting an LED beam. I wrote C++ firmware to collect and log sensor data, tune thresholds, and print droplet events.

## Tools and Skills
- Raspberry Pi Pico (MicroPython)
- ADC reading, PWM, GPIO
- Sensor calibration and thresholding
- Real-time data logging
- Oscilloscope validation of sensor behavior

## Key Contributions
- Implemented analog sampling and programmed real-time detection logic.
- Tuned ADC thresholds and PWM duty cycles for stable readings.
- Tested and graphed sensor response under different lighting conditions.

## Files
- `main.py` (firmware)
- test plots
- wiring diagrams
