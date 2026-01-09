---
title: "Syringe Pump"
excerpt: "DIY syringe pump capable of 1 uL / min flow rate up to 10 mL / min"
header:
  image: /assets/img/Syringepumpphotos/homepage.jpg
  teaser: /assets/img/Syringepumpphotos/homepage.jpg
---

## Project Overview

This DIY syringe pump project demonstrates precision fluid handling capabilities with flow rates ranging from 1 μL/min to 10 mL/min. The pump was designed and built as part of my digital fabrication minor coursework, showcasing both mechanical design and control system integration.

## Technical Specifications

- **Flow Rate Range**: 1 μL/min to 10 mL/min
- **Precision**: High-accuracy microfluidics control
- **Control System**: Programmable stepper motor control
- **Syringe Compatibility**: Standard medical syringes
- **Build Method**: 3D printed components with off-the-shelf hardware

## Off-the-Shelf Components

| Component | Part Number/Description | Quantity |
|-----------|------------------------|----------|
| Ball Bearing | F688ZZ-Flanged-Ball-Bearing v2 | 1 |
| Lead Screw Collar | Lock-Collar-Lead-Screw v5 | 1 |
| Stepper Motor | NEMA-17-Motor v1 | 1 |
| Flexible Coupling | FLEXIBLE COUPLER v2 | 1 |
| End Support | End-Support v8 | 1 |
| Mounting Bolt (5mm) | M5x8mm-Bolt v2 | Multiple |
| Mounting Bolt (3mm) | M3x6mm-Bolt v3 | Multiple |
| Linear Bearing | LM8UU-Linear-Bearing v2 | 2 |
| Mounting Bolt (3mm) | M3x10mm-Bolt v2 | Multiple |
| Linear Rod Collar | Lock-Collar-Linear-Rod v5 | 2 |
| Motor Mount | motor mounting plate v8 | 1 |
| Linear Rod | Linear-Rod-8mmx200mm v2 | 2 |

## Arduino Code

The syringe pump is controlled by an Arduino microcontroller running custom code that manages stepper motor control, flow rate calculations, and LED status indicators.

### Key Features:
- **Flow Rate Control**: Programmable flow rates from 1 μL/min to 10 mL/min
- **LED Status Indicators**: Green (running), Blue (stopped), Red (error)
- **Button Control**: Simple on/off toggle functionality
- **Precision Control**: Microstepping for accurate flow delivery

```cpp
#include <AccelStepper.h>

// Pin definitions
#define stepPin 3 // gray
#define directionPin 2 // orange
#define redLED 5 // red
#define greenLED 6 // green
#define blueLED 7 // blue
#define onOffButton 10 // pink

// Stepper motor setup
AccelStepper stepper(AccelStepper::DRIVER, stepPin, directionPin);

// Variables
bool onOffPressed = false; // Tracks the state of the system (on/off)
float flowRate = 0.5; // mL/min
float syringeDiameter = 19; //20 mL syringe
float syringeRadius = syringeDiameter / 2;
const float leadScrewLead = 8.0; // Lead screw lead in mm/rev
const float stepsPerRevolution = 200.0; // Steps per revolution
const float microsteps = 16.0; // Microstepping factor
float stepsPerSecond = 0.0; // Calculated steps per second
float volumePerStep;

void setup() {
  // Initialize pins
  pinMode(redLED, OUTPUT);
  pinMode(greenLED, OUTPUT);
  pinMode(blueLED, OUTPUT);
  pinMode(onOffButton, INPUT_PULLUP);
  
  // Stepper motor setup
  stepper.setMaxSpeed(1000); // Maximum speed
  stepper.setAcceleration(500); // Acceleration
  
  // Default LED status (blue for stopped)
  updateLEDs();
}

void loop() {
  float volumePerStep = (PI * pow(syringeRadius, 2) * leadScrewLead) /
                        (stepsPerRevolution * microsteps * 1000);
  stepsPerSecond = flowRate / volumePerStep / 60;
  
  // Check and handle the on/off button state
  static bool previousState = HIGH;
  bool currentState = digitalRead(onOffButton);
  
  if (previousState == HIGH && currentState == LOW) {
    onOffPressed = !onOffPressed; // Toggle state
    updateLEDs(); // Update LED based on state
  }
  previousState = currentState;
  
  // Control the motor based on the current state
  if (onOffPressed) {
    stepper.setSpeed(stepsPerSecond); // Set motor speed
    stepper.runSpeed(); // Run the motor
  } else {
    stepper.stop(); // Stop the motor
  }
}

void updateLEDs() {
  if (onOffPressed) {
    // Green LED ON for "ON" state
    digitalWrite(redLED, LOW);
    digitalWrite(greenLED, HIGH);
    digitalWrite(blueLED, LOW);
  } else {
    // Blue LED ON for "OFF" state
    digitalWrite(redLED, LOW);
    digitalWrite(greenLED, LOW);
    digitalWrite(blueLED, HIGH);
  }
}
```

## CAD Model

<iframe src="https://a360.co/4boEFeP?mode=embed" width="100%" height="600px" frameborder="0" allowfullscreen webkitallowfullscreen mozallowfullscreen>
  <p>Your browser does not support embedded CAD models. <a href="https://a360.co/4boEFeP">View CAD Model</a></p>
</iframe>



## Design Features

The syringe pump incorporates several key design elements:

- Precision lead screw mechanism for accurate linear motion
- Stepper motor control for programmable flow rates
- Robust 3D-printed frame and mounting system
- User-friendly interface for flow rate adjustment
- Compact design suitable for laboratory environments

## Applications

This syringe pump is ideal for:
- Microfluidics research
- Precise chemical dispensing
- Laboratory automation

## Final Assembly

![Completed Syringe Pump Assembly](/assets/img/Syringepumpphotos/homepage.jpg){: .align-center width="800" }

*The completed syringe pump showing the final assembled system ready for precision fluid handling applications.*
