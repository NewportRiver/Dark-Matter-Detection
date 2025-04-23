# quantum_separation_framework.py
"""
Starfleet Quantum Framework: Dark Matter Separation Modeling System
This framework visualizes the interaction (or non-interaction) of particles under magnetic,
gravity, and quantum vacuum forces with tunable parameters for experimentation.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# --- Constants ---
c = 3e8  # Speed of light (m/s)
hbar = 1.055e-34  # Reduced Planck constant (J·s)
q = 1.6e-19  # Elementary charge (C)
m_e = 9.11e-31  # Electron mass (kg)
G = 6.674e-11  # Gravitational constant (m^3/kg/s^2)

# --- Derived Forces ---
def lorentz_force(v, B):
    return q * np.cross(v, B)

def gravitational_force(m1, m2, r):
    return G * m1 * m2 / r**2

def casimir_force(a):
    return (np.pi**2 * hbar * c) / (240 * a**4)

# --- Simulation Model ---
def simulate_particles(num=5, field_strength=1.0):
    B = np.array([0, 0, field_strength])  # Tesla, magnetic field along z
    initial_pos = np.random.rand(num, 3) * 1e-2
    velocity = (np.random.rand(num, 3) - 0.5) * 1e5
    mass = np.full(num, m_e)
    charge = np.array([q if i % 2 else 0 for i in range(num)])

    trajectories = np.zeros((100, num, 2))
    for t in range(100):
        for i in range(num):
            if charge[i] != 0:
                a = lorentz_force(velocity[i], B) / mass[i]
                velocity[i] += a * 0.01
            initial_pos[i] += velocity[i] * 0.01
            trajectories[t, i] = initial_pos[i][:2]
    return trajectories

# --- Plot Setup ---
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

initial_B = 1.0
paths = simulate_particles(field_strength=initial_B)
lines = [ax.plot(paths[:, i, 0], paths[:, i, 1], label=f"{'Neutral' if i%2==0 else 'Charged'} {i}")[0] for i in range(paths.shape[1])]

ax.set_title("Quantum Separation Simulation")
ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")
ax.legend()
ax.grid(True)

# --- Slider Control ---
axB = plt.axes([0.2, 0.1, 0.65, 0.03])
slider_B = Slider(axB, 'B Field (T)', 0.1, 5.0, valinit=initial_B)

def update(val):
    B_val = slider_B.val
    new_paths = simulate_particles(field_strength=B_val)
    for i, line in enumerate(lines):
        line.set_xdata(new_paths[:, i, 0])
        line.set_ydata(new_paths[:, i, 1])
    fig.canvas.draw_idle()

slider_B.on_changed(update)

plt.show()