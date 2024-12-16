# Update 5: Prototyping Preparation and New Components

**Date**: December 16, 2024  
**Author**: Daniel Grant  
**Institution**: Bowdoin College  
Advisor: Dr. Laura Toma  

---

## Summary
This week a few critical components for the physical prototyping of my hopping robot will arrive, including a high-torque brushless DC motor and tools like a heat gun and soldering iron. These new additions should help as I begin to build a prototype, and conduct physical testing alongside my CoppeliaSim testing. Preliminary testing in CoppeliaSim confirmed the motor’s suitability for propelling the robot off the ground with a specified payload (details below), reinforcing its potential for use in the final design. Prototyping efforts are in process, with a particular focus on frame assembly, wiring, and joint integration. However, due to final exams and an essay deadline, my overall time commitment this week was/will be slightly reduced compared to previous weeks.

**Time Spent**: 4 hours

---

## Detailed Description

### Component Arrival

1. **Motor**: A high-torque brushless DC motor, comparable (albeit much heavier) to the one used in the Salto-1P robot, arrived this week. This motor is a key component due to its:
   - High power-to-weight ratio, critical for minimizing the overall mass of the robot.
   - Rapid response characteristics
   - Peak torque of 0.8 Nm, which is well-suited for the dynamic and repetitive movements required by single-legged hopping robots.

   Preliminary simulations in CoppeliaSim indicate that the motor is capable of propelling a ~750-gram robot off the ground, achieving a vertical jump height of approximately 5 cm. These results suggest that I can allocate up to 360 grams for an onboard power supply while maintaining optimal performance. Further testing will determine the best distribution of weight to balance efficiency and power.

2. **Heat Gun/Soldering Iron**: The arrival of these tools will be quite helpful as I look towards facilitating wire management, sensor integration, and secure connections for the actuators.

---

### Simulation Insights

#### Motor Performance
Simulated tests conducted in CoppeliaSim yielded some helpful insights:
- The motor functions effectively within a lightweight aluminum frame, working in tandem with a spring-damper system to produce consistent hopping dynamics. Although my frame will be made of 3D printed PLA plastic instead of aluminum, the motor’s performance should remain consistent.
- Load tests confirmed that a power supply weighing up to 360 grams provides sufficient energy for sustained operations, without compromising the robot’s ability to achieve the desired jumping height or maintain stability during motion.
- The integration of sensor feedback into the simulation helped refine the motor’s performance under varying load conditions, allowing adjustments to ensure robust control.

#### Joint Selection
For now, **ball bearings** have been chosen for the robot’s knee and hip joints. These components were selected due to their:
- Low friction, which ensures smooth and efficient rotational motion.
- High durability, capable of withstanding the repetitive impact forces associated with hopping.
- Compact design

Future iterations of the design may explore more advanced joint mechanisms, especially if durability or performance issues arise during extended testing phases.

---

### Prototyping Begins
Initial prototyping efforts started today (Monday, December 16). These early stages focus on building the foundational structure and verifying the compatibility of key components. Specific tasks include:
- Installing the motor and performing initial wiring to test its integration with the frame and control system.
- Implementing the spring-damper system and subjecting it to static load tests to evaluate its performance under various conditions.

Images and videos documenting the prototyping process will be captured and included in the next update, scheduled for Thursday. 

---

### Challenges
- **Time Constraints**: Balancing two final exams and a final essay with prototyping efforts proved challenging, limiting the time available for in-depth experimentation and assembly. Despite this, meaningful progress was made in preparation for the winter break, where the bulk of the prototyping will occur.
- **Weight Distribution**: Determining the optimal balance for the motor, power supply, and sensors within the 750-gram (self-imposed) weight limit required iterative simulations and adjustments. This remains an ongoing area of focus to ensure both performance and stability.

---

### Next Steps
- Complete the initial rough prototype, including testing the hopping mechanics under different loads and surface conditions.
- Finalize the integration of sensors and verify real-time data transmission to the microcontroller, ensuring the control loop operates as intended.
- Document the entire prototyping process with detailed images and videos
- Allocate additional time during the winter break to assemble and thoroughly test the prototype using the new components, with a focus on refining the control algorithms and ensuring structural integrity.

---

### References
- [Salto-1P](https://robotics.berkeley.edu/salto/)  
- [Brushless DC Motor Basics](https://www.motioncontroltips.com/what-is-a-brushless-dc-motor/)  
- [Ball Bearings](https://www.skf.com/group/products/rolling-bearings/ball-bearings)  
- [CoppeliaSim](https://www.coppeliarobotics.com/)  

