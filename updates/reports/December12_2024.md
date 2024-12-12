# Update 4: Simulation Expansion Using CoppeliaSim and Component Selection

**Date**: December 12, 2024  
**Author**: Daniel Grant  
**Institution**: Bowdoin College  
Advisor: Dr. Laura Toma  

## Summary  
This week, I transitioned to using CoppeliaSim for robot modeling and simulation. The platform's versatility and support for integrated physics engines enabled the creation of a more detailed and interactive model of the vertical hopping robot. Additionally, I researched potential components for the physical build and identified suppliers for critical parts.

---

## Detailed Description  

### Simulation Development  
CoppeliaSim was chosen for its scripting capabilities, real-time dynamics simulation, and modular interface. I created a detailed model of the robot, focusing on its spring-damper system and actuators for controlled hopping. The software's support for LUA scripting allowed the integration of basic control algorithms, enabling early testing of dynamic behaviors.

Here is a snapshot of the simulation environment:

![Robot Simulation in CoppeliaSim](https://example.com/coppeliasim-simulation-snapshot.jpg)  

#### Key Features Implemented:
- **Spring-Damper Mechanism**: Modeled to replicate the energy transfer during hopping.  
- **Actuator Simulation**: Virtual actuators were programmed to test vertical hopping under varying force profiles.  
- **Sensor Integration**: Simulated accelerometers and force sensors provided real-time data for control loop development.  
- **Dynamic Terrain**: Explored varied surface conditions like inclines and (un)even terrain.  

---

### Component Selection  
To ensure the physical prototype aligns with the simulated model, I began sourcing components from reliable vendors. Below are some key components and their potential suppliers:

1. **Actuators**: High-torque servo motors for precise control.  
   - [ServoCity Servo Motors](https://www.servocity.com/servos)  

2. **Microcontroller**: Arduino for basic control, with potential Raspberry Pi integration for advanced processing.  
   - [Arduino Uno](https://store.arduino.cc/products/arduino-uno-rev3)  
   - [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)  

3. **Sensors**: Accelerometers and gyroscopes to capture motion data.  
   - [Adafruit MPU6050](https://www.adafruit.com/product/3886)  

4. **Frame Materials**: Lightweight aluminum for structural components.  
   - [McMaster-Carr Aluminum Tubing](https://www.mcmaster.com/aluminum-tubing)  

5. **Power Supply**: Compact battery packs to support high power demands.  
   - [Tenergy Li-ion Battery Pack](https://www.tenergy.com/li-ion-batteries)  

---

### Challenges  
- Fine-tuning the actuator and spring-damper parameters in CoppeliaSim required iterative adjustments to achieve realistic motion.  
- Finding lightweight yet durable components for the frame proved challenging due to availability constraints.  
- Ensuring power supplies met energy needs without compromising portability.  

---

### Next Steps  
- Complete the simulation by integrating a PID-based control system and testing hopping stability on varying terrains.  
- Finalize component procurement to ensure readiness for physical prototyping over the winter break.  
- Begin 3D printing critical parts, leveraging the designs from simulations.

---

### References  
- [CoppeliaSim](https://www.coppeliarobotics.com/)  
- [ServoCity](https://www.servocity.com/)  
- [Adafruit](https://www.adafruit.com/)  
- [McMaster-Carr](https://www.mcmaster.com/)  
- [Tenergy](https://www.tenergy.com/)  

---

