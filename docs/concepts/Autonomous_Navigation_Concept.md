# Autonomous Navigation Concept

## Initial Navigation Strategy

The initial navigation concept uses camera vision to estimate the distance
and angular position of obstacles relative to the robot.

Basic decision logic:

1. If no obstacle is within the minimum avoidance distance, continue forward.
2. If an obstacle is within the avoidance distance:
   - Determine the obstacle's angle relative to the robot/camera centerline.
   - Turn away from the obstacle.
3. Continue measuring distance and angle as the robot moves.
4. Adjust speed based on obstacle distance.
5. Resume forward movement once the path is sufficiently clear.

The initial avoidance distance is approximately 1 foot, but this value
should remain configurable and may change after physical testing.

## Coordinate Reference

A consistent coordinate system must be defined.

Proposed camera-relative system:

- 0 degrees = directly ahead
- Negative angle = obstacle to the left
- Positive angle = obstacle to the right

Example:

             0°
             |
             |
     -45°    |    +45°
          \  |  /
           \ | /
            ROBOT

The robot can use the obstacle's angle relative to the camera centerline
to determine which direction to turn.

## Speed Control

Robot speed may vary based on obstacle distance.

Example behavior:

- Far from obstacle -> normal speed
- Approaching obstacle -> reduced speed
- Inside avoidance threshold -> turn/avoid
- Critically close -> stop or reverse

## Design Considerations

- Fixed camera vs. rotating camera
- Camera field of view
- Camera calibration
- Distance estimation
- Ultrasonic sensor integration
- Robot orientation
- Compass/IMU-based heading
- Wheel/motor odometry
- Course-relative positioning
- Recovery when the robot becomes disoriented
