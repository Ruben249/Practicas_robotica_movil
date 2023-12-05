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
K_REPULSIVE = 0.04
K_REPULSIVE_WALL = 0.3
K_ATTRACTIVE = 0.3
MAX_SPEED = 5.0 
MIN_LINEAR_SPEED = 3.0
MAX_ANGULAR_SPEED = 2.0
ERROR = 1
TURN_RADIUS = 2.5

```
K_REPULSIVE allows us to control the repulsive force of the obstacles. With k we control the repulsive force of the walls, while K_ATTRACTIVE conrol the attractive. TURN_RADIUS is the safe turning radius to avoid collisions. ERROR is the margin of error to find the target

With these variables I managed to make my car behave better, but it still randomly turned 180 degrees and went off the circuit.
![180º](https://github.com/Ruben249/practicas_robotica_movil/assets/102288264/7f0364a9-0264-4246-bcca-22ae4bc036d1)

After a lot of testing, trying to limit the turn, increasing the attractive force, the repulsive force. I realized that the problem was that the target made it turn, since it was quite tilted, but the circuit made him go straight or turn in another direction. 

To solve this problem I decided to create a K_REPULSIVE_WALL just as strong as the K_ATTRACTIVE, so that it does not crash into walls or pass through them.

To make it work better, I decided that without losing reactivity, I would recover the position I had before turning to avoid an obstacle.

These are the constants. 
```python
recovering = False
recovery_counter = 0
recovery_direction = 1 
```
With which we recover the position. If it has detected an obstacle and has turned, in the next 10 iterations of the loop it checks whether it has to continue recovering the position, having previously been aware of whether there is a wall or an obstacle.

Below we have a video in which we see how the car works using everything explained above:

[Video_coche.webm](https://github.com/Ruben249/practicas_robotica_movil/assets/102288264/722e853e-570b-4ddb-8260-4dfe380adec4)
