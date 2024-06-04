# Mobile_Robotics_Practices
## Obstacle_Avoidance
![Portada](https://github.com/Ruben249/practicas_robotica_movil/assets/102288264/a57ba1c5-8658-4a27-a15d-c7e606c27db6)


### Index

-[Start](#start)

-[Development](#development)

-[Conclusion](#conclusion)

#### Start

To begin, we must develop an algorithm with which we expand the map by gradient from the target to the car. For this I decided to use the A* algorithm. This algorithm searches for the shortest path from an initial state to the goal state through a problem space, using an optimal heuristic. Since it ignores the shorter (flatter) steps in some cases it yields a suboptimal solution.

Luckily, in another subject of this degree, artificial intelligent, we have seen this algorithm and how to obtain neighbors, that is why this part has been "simple" for me.

![A*](https://github.com/Ruben249/practicas_robotica_movil/assets/102288264/4eea3241-a4e5-4d34-b005-426d209c7d48)

Here I leave a small part of my star algorithm that we saw in class
```python
def update_grid_with_values(priority_queue, current_item, grid):
    """Update the grid with the values of the neighbors of the current item."""
    current_x, current_y = current_item[1]
    current_value = current_item[0]
    # Define the directions to search for neighbors
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for dx, dy in directions:
        neighbor_x, neighbor_y = current_x + dx, current_y + dy
        # Check if the neighbor is within the grid and if it is not an obstacle
        if 0 <= neighbor_x < 400 and 0 <= neighbor_y < 400 and grid[neighbor_y][neighbor_x] == -1 and map_image[neighbor_y][neighbor_x] != 0:
        ...
        ...
```
#### Development
Development Challenges

#### Map Representation Challenge:

Problem: When converting between the grid-based map representation and the robot's pose, a misalignment issue occurred.

Solution: Careful attention was needed to ensure consistency between the grid coordinates of the map and the real-world coordinates of the robot. Failure to maintain accurate alignment could lead to the robot misinterpreting its position within the environment, affecting path planning and obstacle avoidance.

![MAP](https://github.com/Ruben249/practicas_robotica_movil/assets/102288264/548ae3d8-1454-4247-a7fa-faa4baa5eaa4)

#### Normalize Map Challenge:

Problem: My main problem when dealing with this practice has been being able to normalize the real values ​​with those on the map.

Solution: The solution to normalize the values ​​is to take into account where the car is with respect to the map and its center.

#### Erratic Deviations and Unstable Movements

Problem: Searching for the position with the lowest value is performed in an 11x11 area around the robot. However, the size of the grid and the resolution of the movements can cause the robot to move erratically and with sudden oscillations.

Solution: Reducing the size of the search area or smoothing the transition between cells with different values ​​can improve motion stability. Additionally, adjusting the linear and angular speed of the robot based on the distance and angle to the new position can contribute to smoother navigation.

#### Obstacle Avoidance Challenge:

Problem: The algorithm exhibited erratic behavior around obstacles, sometimes getting too close or overly avoiding them.

Solution: Tuning the obstacle weights was crucial for achieving smooth navigation. If obstacle weights were too low, the robot might collide with obstacles, while excessively high weights could lead to overly cautious navigation. Striking the right balance ensured effective obstacle avoidance without unnecessary deviations.

#### Target Approach Challenge:

Problem: The car struggled to approach the target accurately, either overshooting or getting stuck near the destination.

Solution: Fine-tuning the parameters related to target approach was necessary. Adjusting the speed, turning radius, or control gains during the final approach phase helped achieve a more precise and controlled arrival at the target. Failure to fine-tune these parameters could result in erratic or suboptimal behavior during the final stages of navigation.

![Path](https://github.com/Ruben249/practicas_robotica_movil/assets/102288264/426920ed-b337-45eb-97db-9a2023d15c7b)

#### Angle Calculation

The angle is calculated this way to determine the direction from the object to the lowest point in a Cartesian coordinate system. The arctangent (arctan) function is used because it provides the angle of inclination between two points, which is essential for navigation and orientation of the object.

- **If x is 0**: The angle is set to 90 degrees (pi/2) because the point is directly above or below on the y-axis.
- **If x is not 0**: Arctan is used to calculate the correct angle based on the y/x ratio.

#### Angle Adjustment

Adjusting the angle based on the quadrant is necessary because the arctan function only provides results within a limited range (typically from -π/2 to π/2). Depending on the coordinates of the point, the angle must be adjusted to reflect the correct direction in a full 360-degree coordinate system (or 2π radians).

- **If x is positive**: We adjust the angle to be within the correct range.
- **If x is negative**: Similarly, we adjust the angle to consider the remaining quadrants.

#### Angular Speed Adjustment

The angular speed is adjusted this way to ensure that the object turns in the shortest direction towards the desired angle, keeping the rotation within the range of -π to π radians. This is crucial to avoid unnecessary rotations and to optimize the efficiency of movement.

- **If the angular speed is greater than π**: It is adjusted to reduce the angle to a smaller range.
- **If the angular speed is less than -π**: It is similarly adjusted to maintain efficient rotation.


### Conclusion
Developing a robust route planning algorithm involves addressing several challenges related to mapping, obstacle avoidance, and real-world interface. The A* algorithm, with proper tuning and integration, proves to be a reliable solution for mobile robot navigation, as it allows us to check neighboring nodes and whether or not it would be a good idea to pass by them.


Below I attach a short video of how my program works:

[https://youtu.be/ahlBfqgEtNw](https://youtu.be/RDO-zG-OfKA)
