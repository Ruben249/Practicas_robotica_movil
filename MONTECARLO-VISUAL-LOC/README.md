# Mobile_Robotics_Practices

## Montecarlo Visual Loc

![Title](https://github.com/Ruben249/practicas_robotica_movil/assets/102288264/89ebd672-319e-44b5-accf-150b0cf97873)


### Index
-[Start](#start)

-[Development](#development)


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
Finally, I have taken compute_particle_weights, that I am going to show below, and I have modified it so that the weights depend on the Euclidean distance between the particles and the robot:
```python
def compute_particle_weights(particles):
    """ Compute the weight of each particle.
        This function should generate a virtual laser measurement
        for each particle and compute the error (difference)
        between the virtual laser and the actual sensor measurement.

        This example function just generates random weights.
    """
    weights = np.random.rand(particles.shape[0])
    return weights
```
It should be noted that this is the function that was provided to us and I have modified it so that it calculates the weights using the Euclidean distance.

Here is a video where we briefly see how the robot behaves:

[https://github.com/Ruben249/practicas_robotica_movil/assets/102288264/ba953b52-4f57-4145-97a5-65e79850400a](https://youtu.be/Df01joXrcjY)
