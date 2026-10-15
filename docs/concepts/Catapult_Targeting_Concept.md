# Autonomous Target Detection and Catapult Launch Concept

## Concept Overview

The proposed launch system uses a rotating ultrasonic distance sensor to scan
the area in front of the robot and identify potential ground targets based on
changes in measured distance.

The sensor records both:

- The angle at which the measurement is taken
- The measured distance at that angle

As the sensor sweeps across the environment, the system compares consecutive
distance measurements. A sudden change in measured distance may indicate a
significant feature such as a raised target, depression, opening, or other
change in the ground surface.

Once a target is detected, the robot estimates the target's position relative
to the launching mechanism and calculates the launch parameters required to
reach it.

## Target Detection Strategy

1. Sweep the ultrasonic sensor through a defined angular range.
2. Record the distance measured at each sensor angle.
3. Compare neighboring measurements.
4. Detect significant changes in distance.
5. Determine whether the detected change represents a valid target.
6. Estimate the target's distance and angular position relative to the robot.
7. Pass the target position to the launch-control system.

Example:

    Distance
       ^
       |
       |       normal ground
       |--------------------
       |                   \
       |                    \  sudden change
       |                     \
       +----------------------------> Sensor Angle

A sufficiently large change between measurements can be treated as a
candidate target boundary.

## Launch Calculation

After determining the approximate target position, the launch system calculates
the projectile trajectory required to reach the target.

Important variables include:

- Target distance
- Target position relative to the robot
- Launch angle
- Projectile launch velocity
- Release height
- Gravity
- Mechanical characteristics of the catapult

The system can then determine the required catapult configuration and launch
strength needed to place the projectile near the target.

The initial system may use experimentally calibrated launch settings rather
than relying entirely on theoretical calculations.

## Sensor and Angle Considerations

Certain sensor orientations may produce unreliable measurements.

Possible dead zones include:

- Angles where the ultrasonic sensor points into open space and receives no echo
- Near-vertical sensor orientations
- Angles where the robot itself obstructs the sensor
- Surfaces that reflect ultrasonic waves away from the sensor
- Measurements outside the useful operating range of the sensor

Invalid or missing measurements should be ignored rather than interpreted
directly as targets.

## Launch Sequence

Proposed sequence:

1. Move the sensor to its starting position.
2. Scan through the permitted angular range.
3. Collect distance measurements.
4. Detect significant distance discontinuities.
5. Identify a valid target.
6. Estimate target position and distance.
7. Determine the required launch parameters.
8. Position or configure the catapult mechanism.
9. Launch the projectile.
10. Return the catapult and sensor system to their starting positions.
11. Resume scanning or navigation.

## Calibration

The system will require physical testing to determine the relationship between
catapult input and projectile trajectory.

Calibration data may include:

- Catapult arm position
- Launch angle
- Motor or actuator command
- Projectile launch velocity
- Projectile mass
- Measured landing distance

These measurements can be used to create a lookup table or mathematical model
for selecting launch settings.

## Future Considerations

- Combining ultrasonic sensing with camera vision
- Distinguishing targets from ordinary obstacles
- Automatically estimating target center position
- Accounting for different target heights
- Compensating for sensor measurement noise
- Adjusting launch force based on measured distance
- Using NumPy to process sensor measurements and trajectory calculations
- Determining whether the robot should reposition itself before launching
- Automatically resetting the launcher after each attempt
