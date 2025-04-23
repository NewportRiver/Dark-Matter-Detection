# lorentz_sim.py
"""
Starfleet Simulation Module – Lorentz Force Simulator
Simulates basic charged particle motion through a magnetic field to model separation behavior.
"""

import numpy as np
import matplotlib.pyplot as plt

# === Simulation Parameters ===
num_particles = 100
steps = 500
dt = 0.1  # time step (s)

# Field Parameters (Tesla)
B_field = np.array([0, 0, 1.0])  # Uniform magnetic field in z-direction

# Particle Parameters
charges = np.random.choice([1.6e-19, 0], size=num_particles)  # Some are neutral (dark matter candidates)
masses = np.full(num_particles, 9.11e-31)  # Electron mass (kg)

# Initial Positions and Velocities
positions = np.random.rand(num_particles, 3) * 1e-2  # meters
velocities = (np.random.rand(num_particles, 3) - 0.5) * 1e5  # m/s

# === Storage for Visualization ===
trajectories = np.zeros((steps, num_particles, 3))

# === Lorentz Force Function ===
def lorentz_force(q, v, B):
    return q * np.cross(v, B)

# === Simulation Loop ===
for t in range(steps):
    for i in range(num_particles):
        if charges[i] != 0:
            F = lorentz_force(charges[i], velocities[i], B_field)
            a = F / masses[i]
            velocities[i] += a * dt
        positions[i] += velocities[i] * dt
    trajectories[t] = positions

# === Visualization (2D X-Y) ===
plt.figure(figsize=(8, 6))
for i in range(num_particles):
    plt.plot(trajectories[:, i, 0], trajectories[:, i, 1],
             label=f'Particle {i}' if charges[i] == 0 else None,
             color='magenta' if charges[i] == 0 else 'cyan', alpha=0.7)

plt.title("Charged vs Inert Particle Motion in Magnetic Field")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.grid(True)
plt.legend(loc='upper right', fontsize='small')
plt.tight_layout()
plt.show()
