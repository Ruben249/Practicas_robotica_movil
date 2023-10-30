# Mobile_Robotics_Practices
## Obstacle_Avoidance
![Portada](https://github.com/Ruben249/practicas_robotica_movil/assets/102288264/ce136c98-b72c-49d2-8ba7-882bff1eb5e7)


### Index

-[Start](#start)

-[Development](#development)

#### Start
The beginning of this practice was easier, since we were more accustomed to the environment and the handling of the car thanks to the p2.
The first problem was to convert the target points on the map to x and y points according to the car, and for this we used a function that we provided.
```python
def absolute2relative (x_abs, y_abs, robotx, roboty, robott):

    # robotx, roboty are the absolute coordinates of the robot
    # robott is its absolute orientation
    # Convert to relatives
    dx = x_abs - robotx
    dy = y_abs - roboty

    # Rotate with current angle
    x_rel = dx * math.cos (-robott) - dy * math.sin (-robott)
    y_rel = dx * math.sin (-robott) + dy * math.cos (-robott)

    return x_rel , y_rel
```

Afterwards, I decided to create a function that would detect if we were on the target, with a small margin of error.
```python
def is_at_target(robot_x, robot_y, target_x, target_y, error=0.2):
    distance_to_target = math.sqrt((robot_x - target_x)**2 + (robot_y - target_y)**2)
    return distance_to_target < error
```

With the following function, we can graphically represent the repulsive force and the direction of the car, but changing the data to real ones
```python
# Car direction  (green line in the image below)
carForce = [2.0, 0.0]
# Obstacles direction (red line in the image below)
obsForce = [0.0, 2.0]
# Average direction (black line in the image below)
avgForce = [-2.0, 0.0]

GUI.showForces(carForce, obsForce, avgForce)
```
#### Development
Once I managed to convert the obstacles and walls into repulsive forces and the target into attractive force, I encountered another problem, and that is that sometimes when passing the obstacles it crashes anyway. That's why I decided to create some global variables to improve overtaking.

```python
K_REPULSIVE = 0.05
K_ATTRACTIVE = 0.3
MIN_LINEAR_SPEED = 2.0
MAX_LINEAR_SPEED = 8.0
ERROR = 0.2
TURN_RADIUS = 2.5
```
K_REPULSIVE allows us to control the repulsive force, while K_ATTRACTIVE the attractive. TURN_RADIUS is the safe turning radius to avoid collisions. error is the margin of error to find the target

With these variables I managed to make my car behave better, but it still randomly turned 180 degrees and went off the circuit.
![180º](https://github.com/Ruben249/practicas_robotica_movil/assets/102288264/7f0364a9-0264-4246-bcca-22ae4bc036d1)


Here is a video where we briefly see how the car behaves.

[FollowLine_Simple.webm](https://github.com/Ruben249/practicas_robotica_movil/assets/102288264/2c9a9c66-92af-472b-bf55-7fa6d0fcbe95)

