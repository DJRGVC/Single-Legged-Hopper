# Update 3: Advanced Simulation Development and Testing Framework  

**Date**: December 9, 2024  
**Author**: Daniel Grant  
**Institution**: Bowdoin College  
Advisor: Dr. Laura Toma

## Summary  
This week, I focused on expanding the simulation model for the vertical hopping robot, emphasizing detailed kinematic behavior and initial control algorithm testing. I also developed a comprehensive testing framework to evaluate the robot's simulated performance and explored tools for generating realistic environments for future trials.

## Detailed Description  

### Overview  
The simulation environment has been expanded to model the robot’s dynamics with greater fidelity. Efforts included implementing a spring-mass system, actuator response, and sensor data simulation to mimic real-world performance. A preliminary control system has been integrated into the simulation, enabling early testing of vertical hopping behaviors.

### Progress  

1. **Simulation Development**:  
   - Refined the Gazebo simulation to include a more accurate spring-mass model for vertical hopping.  
   - Added virtual sensors to simulate accelerometer and force feedback, providing data for control system tuning.  
   - Implemented a simplified terrain model to test hopping stability under different conditions.  

2. **Control System Design**:  
   - Began developing a PID-based control system for achieving stable vertical hopping.  
   - Simulated the control algorithms, focusing on energy efficiency and response time.  

3. **Testing Framework**:  
   - Designed a framework for evaluating simulation results, including metrics for stability, jump height, and energy consumption.  
   - Integrated data logging into the simulation to analyze sensor outputs and actuator performance.  


   Images/videos of simulation results to be added at a later date here.

### Challenges  
- Fine-tuning the simulated spring-mass parameters to match expected physical performance required multiple iterations.  
- Ensuring the simulated sensor data was realistic posed challenges, particularly in replicating noise levels and time delays.  

### Next Steps  
- Complete initial simulation testing to validate the control algorithms.  
- Expand the simulation to include more complex scenarios, such as uneven terrain or lateral forces.  
- Begin planning the transition from simulation to CAD modeling for eventual physical prototyping.  
- Be 100% prepared to begin physical prototyping once I have returned home, as most of my components are there, alongside the 3D printer, and spare tools collected from electrical engineering collegues at UCB. 

### References
- [Previous Update](December2_2024.md)
- [PID Control System](https://en.wikipedia.org/wiki/PID_controller)
- [Gazebo Simulation Environment](http://gazebosim.org/)
- [ROS (Robot Operating System)](https://www.ros.org/)
- [Spring-Mass Model](https://en.wikipedia.org/wiki/Spring%E2%80%93mass_system)
- [Sensor Simulation](https://mitsloan.mit.edu/LearningEdge/simulations/sensor-simulation/Pages/default.aspx)
- [Actuator Response](https://www.sciencedirect.com/topics/engineering/actuator-response)

---
 

