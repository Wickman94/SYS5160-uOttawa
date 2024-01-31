# -*- coding: utf-8 -*-
import numpy as np
from scipy.signal import lti, step

# PSO initialization and parameters
num_particles = 30
num_iterations = 50
cognitive_coef = 1.5
social_coef = 1.5
inertia_weight = 0.9
dim = 5  # Number of parameters to optimize

# Initialize particles
particles = np.random.rand(num_particles, dim) * 10  # Initial positions
velocities = np.random.rand(num_particles, dim) * 1  # Initial velocities

# Initialize personal best positions and their corresponding fitness
p_best_positions = particles.copy()
p_best_fitness = [float('inf')] * num_particles

# Initialize global best position and its corresponding fitness
g_best_position = np.zeros(dim)
g_best_fitness = float('inf')

# Simulate system response (assuming this is the actual system response)
# Define system
system = lti([13, 9], [1, 5, 17, 11])
# Time points
t = np.linspace(0, 10, 1000)
# Simulate step response
_, actual_response = step(system, T=t)

# Objective function (Mean Squared Error between the actual system response and the model's response)
def objective_function(params):
    # Define the system with the current model parameters
    num = [params[0], params[1]]
    den = [1, params[2], params[3], params[4]]
    sys = lti(num, den)
    # Simulate step response
    _, model_response = step(sys, T=t)
    # Calculate MSE
    mse = np.mean((actual_response - model_response) ** 2)
    return mse

# PSO algorithm
for i in range(num_iterations):
    for j in range(num_particles):
        fitness = objective_function(particles[j])

        # Update personal best
        if fitness < p_best_fitness[j]:
            p_best_fitness[j] = fitness
            p_best_positions[j] = particles[j]

        # Update global best
        if fitness < g_best_fitness:
            g_best_fitness = fitness
            g_best_position = particles[j]

        # Update velocity and position
        velocities[j] = (inertia_weight * velocities[j] +
                         cognitive_coef * np.random.rand() * (p_best_positions[j] - particles[j]) +
                         social_coef * np.random.rand() * (g_best_position - particles[j]))
        particles[j] += velocities[j]

# Print the best parameters and the best fitness
print("Best Parameters:", g_best_position)
print("Best Fitness:", g_best_fitness)
