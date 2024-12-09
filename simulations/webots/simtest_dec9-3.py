#include <webots/robot.h>
#include <webots/motor.h>
#include <webots/distance_sensor.h>

#define TIME_STEP 64 (ms)

int main() {
  // initialize Webots
  wb_robot_init();

  // get handle and enable distance sensor
  WbDeviceTag ds = wb_robot_get_device("ds");
  wb_distance_sensor_enable(ds, TIME_STEP);
  
  // get handle and initialize the motors
  WbDeviceTag left_motor = wb_robot_get_device("left_motor");
  WbDeviceTag right_motor = wb_robot_get_device("right_motor");
  wb_motor_set_position(left_motor, INFINITY);
  wb_motor_set_position(right_motor, INFINITY);
  wb_motor_set_velocity(left_motor, 0.0);
  wb_motor_set_velocity(right_motor, 0.0);

  // control loop
  while (1) {
    // read sensors
    double v = wb_distance_sensor_get_value(ds);

    // if obstacle detected
    if (v > 512) {
      // turn around
      wb_motor_set_velocity(left_motor, -600);
      wb_motor_set_velocity(right_motor, 600);
    }
    else {
      // go straight
      wb_motor_set_velocity(left_motor, 600);
      wb_motor_set_velocity(right_motor, 600);
    }
    
    // run a simulation step
    wb_robot_step(TIME_STEP);
  }

  wb_robot_cleanup();
  return 0;
}
