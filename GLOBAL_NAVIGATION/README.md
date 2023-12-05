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
def astar(start, target, obstacles, map_data):
    while priority_queue:
        cost, current = heapq.heappop(priority_queue)

        if current == target:
            break

        if current in visited_cells:
            continue

        visited_cells.add(current)

        neighbors = get_neighbors(current, rows, cols)

        for neighbor in neighbors:
            if neighbor in obstacle_coordinates:
            else:

            if neighbor not in visited_cells:

    path = reconstruct_path(start, target, visited_cells)
    return path
```
#### Development
Development Challenges

-Map Representation Challenge:

Problem: When converting between the grid-based map representation and the robot's pose, a misalignment issue occurred.

Solution: Careful attention was needed to ensure consistency between the grid coordinates of the map and the real-world coordinates of the robot. Failure to maintain accurate alignment could lead to the robot misinterpreting its position within the environment, affecting path planning and obstacle avoidance.

![MAP](https://github.com/Ruben249/practicas_robotica_movil/assets/102288264/548ae3d8-1454-4247-a7fa-faa4baa5eaa4)


-Obstacle Avoidance Challenge:

Problem: The algorithm exhibited erratic behavior around obstacles, sometimes getting too close or overly avoiding them.

Solution: Tuning the obstacle weights was crucial for achieving smooth navigation. If obstacle weights were too low, the robot might collide with obstacles, while excessively high weights could lead to overly cautious navigation. Striking the right balance ensured effective obstacle avoidance without unnecessary deviations.

-Target Approach Challenge:

Problem: The robot struggled to approach the target accurately, either overshooting or getting stuck near the destination.

Solution: Fine-tuning the parameters related to target approach was necessary. Adjusting the speed, turning radius, or control gains during the final approach phase helped achieve a more precise and controlled arrival at the target. Failure to fine-tune these parameters could result in erratic or suboptimal behavior during the final stages of navigation.
![Path](https://github.com/Ruben249/practicas_robotica_movil/assets/102288264/426920ed-b337-45eb-97db-9a2023d15c7b)



With the checkTarget function we check if we have reached the target and the program ends
```python
def checkTarget(target, error=0.5):
    # Check if the robot is close to the target
    # ...
    return result
```

### Conclusion
Developing a robust path planning algorithm involves addressing various challenges related to map representation, obstacle avoidance, and real-world interfacing. The A* algorithm, with proper tuning and integration, proves to be a reliable solution for mobile robot navigation.


Below I attach a short video of how my program works:
https://youtu.be/ahlBfqgEtNw
