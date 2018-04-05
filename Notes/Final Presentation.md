# Final Presentation

## Introduction

- Rico
- Jake
- Adam

## Project Overview

// What does it do?
// How does it accomplish this?
// Why do this?

## Systems Overview

Summarize how each component works.

[image for system here]

- Array Sensors
- Arduino
- Raspberry Pi
  - Conversion Algorithm
  - LED Controller
- LEDs

## Demo

[video]

## Goals + Obstacles

// What we set out to do and what we accomplished.
// how we overcame them.

We set out to create an area where we could track people walking across it, light up LEDs showing where they were, accurately and in real-time.

We encountered many obstacles along the way.

**Jake:** How to parse sensor data and get an accurate position of where the persons would be.

We were not getting accurate readings, and the wrong lights would turn on.

- We removed outliers from the data, and averaged the sensor data
- We created an algorithm to triangulate the position based of the sensor data
  - This involved analyzing different boundary conditions and invalid solutions

**Adam:** Using library for outdated RPi and Neopixel LEDs.

The library provided by Adafruit (the LED manufacturers) did not work very well. We could not properly control the colours of the lights, or specific LEDs.

- We decided to only use white, since it was the only solid colour we could use
- We turned on three LEDs at a time, this also made it easier to see where the tracked person is
- We had to disable the soundcard on the RPi since it interferred with the PWM output of the RPi

## Conclusion

// What we accomplished

We are able to track users with decent accuracy within our 45 cm prototype ring.

// What we could have done better

Tracking would be more accurate:

- with using more ultrasonic sensors
- improving our algorithms
- using infrared sensors, or some other more accurat e technology

We wanted to add more patterns, like eminating from the person's location

- like a ripple pattern

Integrate the project with the other team, but due to time constraints we were unable to start this
