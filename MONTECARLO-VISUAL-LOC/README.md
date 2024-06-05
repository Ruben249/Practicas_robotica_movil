# Mobile_Robotics_Practices

## Montecarlo Visual Loc

![Title](https://github.com/Ruben249/practicas_robotica_movil/assets/102288264/89ebd672-319e-44b5-accf-150b0cf97873)


### Index
-[Start](#start)

-[Development](#development)

-[Conclusion](#conclusion)


#### Start
To carry out this practice, I have not used unibotics, but rather I have used python directly. For this they have provided us with the GUI and HAL libraries, in addition to the map and other files with code.
![Screenshot from 2024-04-29 20-12-47](https://github.com/Ruben249/practicas_robotica_movil/assets/102288264/977f1416-91a8-4016-a2b8-25373c8b0d67)

#### Development
Below I am going to explain the functions that have been provided to us and that I have used:

update_particle_pose(): Update the pose of a particle in the dt period and add a random Gaussian noise to the movement.
```python
def update_particle_pose(particle, dt):
    yaw = particle[2]
    # Estimate robot movement in dt according to the set velocities
    dx = dt * LINEAR_VEL * np.cos(yaw)
    dy = dt * LINEAR_VEL * np.sin(yaw)
    dyaw = dt * ANGULAR_VEL
    # Add this movement to the particle, with an extra Gaussian noise
    particle[0] += dx + np.random.normal(0.0, 0.02)
    particle[1] += dy + np.random.normal(0.0, 0.02)
    particle[2] += dyaw + np.random.normal(0.0, 0.01)
```

def getLaserData(self): Returns the measurements from the laser sensor. Also returns a list of (x,y) points in global world coordinates.
```python
    # Get the robot pose in map coordinates as the origin of the laser
    start_x, start_y, robot_yaw_map = MAP.worldToMap(*self.pose)
    # Convert the maximum laser detection distance from meters to map cells
    laser_distance_cells = MAX_LASER_DISTANCE * MAP.MAP_SCALE
    virtual_laser_xy = []
    for beam_angle in range(180):
        # Angle of the current beam in map coordinates
        angle = robot_yaw_map + np.radians(beam_angle) - np.pi/2
        # Calculate the theoretical (maximum) end point of the laser
        end_x = start_x + laser_distance_cells * np.cos(angle)
        end_y = start_y + laser_distance_cells * np.sin(angle)
        # Get the laser measurement
        laser_x, laser_y = self.virtual_laser_beam(start_x, start_y, end_x, end_y)
        virtual_laser_xy.append((laser_x, laser_y, 0))
    world_laser_xy = MAP.mapToWorldArray(np.array(virtual_laser_xy))
    return world_laser_xy
```

propagate_particles(): Estimate the movement of the robot since the last update and propagate the pose of all particles according to this movement.
```python
def propagate_particles(particles):
    global last_update_time
    # Get the time diference since the last update
    current_time = time.time()
    dt = current_time - last_update_time
    # Update all particles according to dt
    for p in particles:
        update_particle_pose(p, dt)
    # Reset the update time
    last_update_time = current_time
    return particles
```

update_particles(): Update the pose of all particles with a given movement.
```python
def update_particles(particles, delta_x, delta_y, delta_theta):
    for p in particles:
        noise_x = random.gauss(delta_x, 0.1)
        noise_y = random.gauss(delta_y, 0.1)
        noise_theta = random.gauss(delta_theta, 0.05)

        p[0] += noise_x
        p[1] += noise_y
        p[2] = (p[2] + noise_theta) % (2 * math.pi)
```

resample_particles(): Resample the set of particles given their weights.
```python
def resample_particles(old_particles, weights):
    """ Resample the set of particles given their weights. """
    # Allocate space for new particles
    particles = np.zeros((N_PARTICLES, 3))

    # Normalize the weights so the total sum is 1
    weights /= np.sum(weights)
    print(F"Normalized weights: {weights}")

    # Get random indices from the list of particles
    selected_idx = np.random.choice(N_PARTICLES, replace=True, size=N_PARTICLES, p=weights)
    print(F"Selected indices:\n{selected_idx}")
    print(F"Selected particles:\n{old_particles[selected_idx]}")
    particles = old_particles[selected_idx]
    return particles
```

virtual_laser_beam(): Generate a virtual laser beam from the start to the end point. Returns the first obstacle point in the map.
```python
def virtual_laser_beam(start_x, start_y, end_x, end_y):
    # Find the differences between the start and end points
    dx = int(abs(end_x - start_x))
    dy = int(abs(end_y - start_y))
    # Number of steps to take
    steps = max(dx, dy)

    # Calculate the increment for each step
    dx = (end_x - start_x) / steps
    dy = (end_y - start_y) / steps

    # Start at the initial point
    for i in range(steps):
        # Calculate the next point
        x = int(start_x + dx * i)
        y = int(start_y + dy * i)
        # Check if the point is an obstacle
        if 0 <= x < map.shape[1] and 0 <= y < map.shape[0]:
            if map[y, x] == OBSTACLE_VALUE:
                return (x, y)
        else:
            break

    return (np.inf, np.inf)
```
initialize_particles(): Generate random particles in world coordinates (meters) X/Y values are constrained within the map limits.
Yaw values are in the [0, 2*pi] range.
```python
def initialize_particles():
    # Allocate space
    particles = np.zeros((N_PARTICLES, 4))
    # Get the limits from the MAP module
    x_low, y_low = MAP.WORLD_LIMITS_LOW
    x_high, y_high = MAP.WORLD_LIMITS_HIGH
    # Distribute randomly in the map
    particles = np.random.uniform(low=[x_low, y_low, 0.0],
                                  high=[x_high, y_high, 2*np.pi],
                                  size=(particles.shape[0], 3))
    return particles
```
Finally, I have taken compute_particle_weights, that I am going to show below, and I have modified it so that the weights depend on the Euclidean distance between the particles and the laser data:
```python
def compute_particle_weights(particles):
    """ Compute the weight of each particle.
        This function should generate a virtual laser measurement
        for each particle and compute the error (difference)
        between the virtual laser and the actual sensor measurement.

        This example function just generates random weights.
    """
    ...
    ...
    ...
    weights = np.random.rand(particles.shape[0])
    return weights
```

I also had to create a copy of the function function and modify it, to be able to obtain the laser data of each of the particles and make the Euclidean distance.
```python
def getLaserData(particle):
    """ Returns the measurements from the laser particle.
        Returns a list of (x,y) points in global world coordinates.
    """
    start_x, start_y, particleyaw_map = MAP.worldToMap(particle[0], particle[1], particle[2])
    ...
    ...
    ...
    weights = np.random.rand(particles.shape[0])
    return weights
```

### Conclusion
The biggest difficulties that I have encountered in this practice have been knowing which functions to take, which ones to modify and being able to compare the robot laser data with that of the particles, since we had to use a function that allowed us to go from the simulated laser to a more realistic one. Once done, making the Euclidean distance of both has been quite simple for me.

Here is a video where we briefly see how the robot behaves:
[(https://youtube.com/shorts/s-XAeOmATE8?feature=share)](https://youtu.be/F8PqM433ETM)
