# quantum_gui_sim.py
"""
Quantum Separation GUI Simulation – MVP Edition (3D Ready)
This script wraps the MVP simulation in a GUI with real-time controls and an embedded 3D canvas (via vpython).
"""

import tkinter as tk
from tkinter import ttk
from vpython import canvas, vector, sphere, rate, color
import numpy as np
import threading

# --- Physics Constants ---
c = 3e8
hbar = 1.055e-34
q = 1.6e-19
m_e = 9.11e-31

# --- Simulation Settings ---
NUM_PARTICLES = 10
TIME_STEP = 0.01

# --- Initialize GUI ---
root = tk.Tk()
root.title("Quantum Separation Simulator - GUI")
root.geometry("400x300")

# --- 3D Scene ---
scene = canvas(title='Quantum Particle Chamber', width=800, height=600, background=color.black)
scene.camera.pos = vector(0, 0, 0.2)
scene.camera.axis = vector(0, 0, -1)

# --- Particle Class ---
class QuantumParticle:
    def __init__(self, is_charged):
        self.charge = q if is_charged else 0
        self.mass = m_e
        self.pos = vector(np.random.uniform(-0.01, 0.01), np.random.uniform(-0.01, 0.01), 0)
        self.vel = vector(np.random.uniform(-1e5, 1e5), np.random.uniform(-1e5, 1e5), 0)
        self.sphere = sphere(pos=self.pos, radius=0.002, make_trail=True,
                             color=color.cyan if is_charged else color.magenta)

    def update(self, B):
        if self.charge != 0:
            F = self.charge * self.vel.cross(B)
            a = F / self.mass
            self.vel += a * TIME_STEP
        self.pos += self.vel * TIME_STEP
        self.sphere.pos = self.pos

# --- Particle System ---
particles = [QuantumParticle(i % 2 != 0) for i in range(NUM_PARTICLES)]
B_field = vector(0, 0, 1.0)  # Default magnetic field

# --- Simulation Runner ---
running = True
def run_simulation():
    while running:
        rate(60)
        for p in particles:
            p.update(B_field)

# --- Start Simulation Thread ---
sim_thread = threading.Thread(target=run_simulation)
sim_thread.start()

# --- GUI Controls ---
def update_field(val):
    global B_field
    try:
        B_val = float(val)
        B_field = vector(0, 0, B_val)
    except ValueError:
        pass

def stop_sim():
    global running
    running = False
    root.quit()

# Magnetic Field Slider
ttk.Label(root, text="Magnetic Field (Tesla):").pack(pady=10)
field_slider = ttk.Scale(root, from_=0.1, to=5.0, orient='horizontal', command=update_field)
field_slider.set(1.0)
field_slider.pack(pady=10)

# Exit Button
ttk.Button(root, text="End Simulation", command=stop_sim).pack(pady=20)

# Run GUI loop
root.mainloop()
