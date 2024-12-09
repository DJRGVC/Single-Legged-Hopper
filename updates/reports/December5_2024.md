# Update 2: Initial Robot Design, Material Procurement, and 3D Print Testing

**Date**: December 5, 2024  
**Author**: Daniel Grant  
**Institution**: Bowdoin College  
Advisor: Dr. Laura Toma

## Summary  
The last few days marked the beginning of the robot design process. I focused on developing a CAD model for a simple vertical hopping prototype and identifying the materials needed for the initial build. 

I have not had significant experience with 3D printing before--as such, as a late birthday present for myself, I decided to purchase the following 3D printer:

![Prusa Mk4](https://www.prusa3d.com/product/original-prusa-mk4s-3d-printer-kit/)

Once it arrived, I spent a few days learning how to use it and testing different materials and settings. I have listed my prints below. I additionally conducted a basic test of printing my own designs, and managed to produce a print of reasonable quality.


## Detailed Description  

### Overview  
The simple hopping model is inspired by Raibert’s planarized systems, incorporating a spring-mass mechanism with actuators for controlled movement. CAD work emphasized modularity to facilitate iterative design improvements. More info below on my design, printing tests, and next steps.

### Progress  

1. **Design Work**:  
   - Drafted a CAD model featuring a lightweight frame, spring-damper system, and sensor mounts.  
   - Designed the model with modular joints to accommodate future upgrades, such as additional degrees of freedom for planar hopping.  

2. **Procurement**:  
   - Began compiling a comprehensive list of components, including an Arduino microcontroller, servo motors, sensors, and connectors (most of which I already have! But, considering a Raspberry Pi for more complex control for now...).

3. **Software Planning**:  
   - Outlined the initial control system architecture, focusing on vertical hopping using PID controllers (on the Arduino) for actuator control.

### 3D Printing Tests

1. **Test Prints**:  

I printed six objects, four of which are listed below, to test a variety of materials and settings:

- **Print 1**: A Flying Ring, testing the printer's vase mode for a smooth, continuous print.  
  ![Flying Ring](https://www.printables.com/model/405983-hollow-flying-ring-long-distance-spiral-toy)  
 
- **Print 2**: A catapult, testing the printer's ability to print complex, moving parts.  
  ![Catapult](https://www.printables.com/model/977936-catapult-snap-fit-model)

  - **Print 3**: A small, light plane, testing the printer's ability to print small, detailed objects.                
  ![Plane](https://www.printables.com/model/430012-ultralight-2gram-glider-print-in-place/files)

- **Print 4**: Concentric Rings, testing the printer's ability to print moving parts.  
![Concentric Rings](https://www.printables.com/model/972886-rotarings-print-in-place-rotating-fidget/files)

Finally, I designed and printed a basic phone case, as an introduction to Fusion 360 and 3D printing. The print was successful, using PLA filament with a 0.2mm layer height and 20% infill, and a hexagonal back pattern for added strength.

I also managed to test and print a basic frame to contain the robot's components. This seems to be a good starting point for the robot's design, and I am excited to continue working on it. It fit well around the small solenoid I had on hand that I designed it for, and I am excited to continue working on it.

I did get someone carried away here, but I am excited to have a 3D printer to help with the project!

### Challenges  
- Finding high-torque yet lightweight actuators suitable for the robot's compact frame proved difficult. Prior tests with solenoids and linear actuators were unsuccessful.
- Delays in component delivery could impact the assembly timeline, requiring adjustments to the project schedule. Hoping to find a local solution as I begin to build over the winter break.

### Next Steps  
- Finalize the CAD model and prepare STL files for 3D printing.  
- Begin assembling the mechanical frame as parts arrive.  
- Implement and test initial control algorithms using simulated data. 

### References 

- Raibert, M. H. (1986). Legged robots that balance. MIT Press.
- Prusa Research. (2024). Original Prusa MK4S 3D Printer Kit. Retrieved from [https://www.prusa3d.com/product/original-prusa-mk4s-3d-printer-kit/](https://www.prusa3d.com/product/original-prusa-mk4s-3d-printer-kit/)
- CAD Design Software. (2024). Fusion 360. Autodesk. Retrieved from [https://www.autodesk.com/products/fusion-360/overview](https://www.autodesk.com/products/fusion-360/overview)
- Printables. (2024). Flying Ring. Retrieved from [https://www.printables.com/model/405983-hollow-flying-ring-long-distance-spiral-toy](https://www.printables.com/model/405983-hollow-flying-ring-long-distance-spiral-toy)
- Printables. (2024). Catapult. Retrieved from [https://www.printables.com/model/977936-catapult-snap-fit-model](https://www.printables.com/model/977936-catapult-snap-fit-model)
- Printables. (2024). Small Plane. Retrieved from [https://www.printables.com/model/430012-ultralight-2gram-glider-print-in-place/files](https://www.printables.com/model/430012-ultralight-2gram-glider-print-in-place/files)
- Printables. (2024). Concentric Rings. Retrieved from [https://www.printables.com/model/972886-rotarings-print-in-place-rotating-fidget/files](https://www.printables.com/model/972886-rotarings-print-in-place-rotating-fidget/files)
