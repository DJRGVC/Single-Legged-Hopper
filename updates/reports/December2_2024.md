# Update 1: Literature Review and Simulation Tool Familiarization  

**Date**: December 2, 2024  
**Author**: Daniel Grant  
**Institution**: Bowdoin College  
Advisor: Dr. Laura Toma

## Summary  
This weekend, and some weeks prior, I concentrated on reviewing foundational research by Marc Raibert and collaborators, which underpins the one-legged hopping robot project. I also began familiarizing myself with simulation tools, including Gazebo and Webots, to evaluate their suitability for modeling the robot’s movements in a virtual environment. By the end of the week, I developed a clearer understanding of how to adapt these tools to simulate the robot’s dynamics effectively.

My initial design document, alongside literature review, is linked here:

[Link to Literature Review](../Literature_Review.pdf)

Time Spent: 13 hrs

## Detailed Description  

### Overview  
The literature review primarily focused on Raibert’s work on dynamically stable legged locomotion, which emphasizes energy-efficient hopping and control systems. Additional materials from nonlinear control research provided insights into designing a robust feedback loop for stability.  

Simulation environments were chosen based on their compatibility with ROS and their ability to handle real-time simulations of complex physical systems. I explored their features through small-scale prototypes and tested basic models to understand their capabilities.

### Progress  

1. **Literature Review**:  
   - Read several reports detailing the mechanical and control aspects of Raibert’s hopping robots.  
   - Reviewed supporting texts on trajectory planning and real-time control strategies, specifically from Slotine and Li's *Applied Nonlinear Control*.  

2. **Simulation Exploration**:  
   - Created simple models of a spring-loaded inverted pendulum (SLIP) to test Gazebo and Webots.  
   - Assessed Gazebo’s physics engine for its precision in dynamic simulations and Webots’ ease of use for iterative design testing.  

3. **ROS Integration**:  
   - Began setting up ROS (2) nodes to interact with the simulation tools. Preliminary testing showed good compatibility with both platforms.

### Challenges  
- Setting up Gazebo required resolving multiple dependency issues due to version mismatches.  
- Discrepancies in how actuators are modeled between Gazebo and Webots complicated the direct comparison.  


### Next Steps  
- Finalize the choice of simulation environment for future development. Tending to lean in the direction of Gazebo due to its robust physics engine, and it is frankly more fun to use!
- Begin drafting the CAD model for the robot’s physical structure and initiate software planning for control algorithms.  
- Expand the literature review to include recent advances in SLAM for potential 3D navigation extensions (long-term goal--not immediate priority).

### References
- Raibert, M. H., & Brown, H. B. (1984). Experiments in balance with a 3D one-legged hopping machine. *The International Journal of Robotics Research, 3*(2), 75-92.
- Slotine, J. J., & Li, W. (1991). *Applied Nonlinear Control*. Prentice Hall.
- Koenemann, J., & Beetz, M. (2015). The Robotic Operating System (ROS). In *Handbook of Robotics* (pp. 335-359). Springer, Cham.
- Gerkey, B. P., & Howard, A. (2009). The Player/Stage Project: Tools for Multi-Robot and Distributed Sensor Systems. In *Proceedings of the International Conference on Advanced Robotics* (pp. 317-323). IEEE.
- Michel, O., & Chatila, R. (2004). Webots: Professional Mobile Robot Simulation. *Journal of Advanced Robotics, 18*(7), 849-858.
- Todorov, E., Erez, T., & Tassa, Y. (2012). Mujoco: A physics engine for model-based control. In *2012 IEEE/RSJ International Conference on Intelligent Robots and Systems* (pp. 5026-5033). IEEE.
- Koenig, N., & Howard, A. (2004). Design and use paradigms for Gazebo, an open-source multi-robot simulator. In *2004 IEEE/RSJ International Conference on Intelligent Robots and Systems* (IROS) (pp. 2149-2154). IEEE.




