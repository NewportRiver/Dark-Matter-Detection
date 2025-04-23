🧪 Dark Matter Quantum Chamber Simulation

This project is a theoretical, interactive simulation environment designed to visually and conceptually demonstrate a novel approach to detecting dark matter using non-collisional magnetic and gravitational separation.

Built in the spirit of open-source exploration, this Starfleet-style research interface blends:
Quantum physics theory
Particle simulation and visualization
Black hole-inspired aesthetics
Scrollable narrated documentation


📁 File Structure

Dark-Matter-Detection/
├── index.html               # Main interactive UI simulation
├── DarkMatter.png           # Background visual (black hole parallax)
├── blackhole.jpg            # Lens shader background image
├── audio/DarkMatter.mp3     # Narration audio file (theory overview)
├── particle_orbit.js        # Included in <script> (lens and orbit logic)
├── style.css (inlined)      # Simulation visuals, particles, mobile-fix
├── quantum_framework_mvp.py # Python backend simulation framework (Lorentz, tunneling, CSV export)
├── casimir_shift_analysis.R # R-based vacuum force analysis stub
├── narration_transcript.txt # Full text version of all narrated theory pages
├── LICENSE                  # MIT License
└── README.md                # This file

🌌 Requirements
This is a front-end HTML+JS simulation and runs entirely in a browser.

To view the simulation:
Open index.html in any modern browser (Chrome, Edge, Firefox, Safari)
Ensure DarkMatter.png and blackhole.jpg are in the same folder
Optional: place the audio/DarkMatter.mp3 in the correct path to enable voice playback
If you wish to run the Python-based simulation backend (quantum_framework_mvp.py):

🐍 Python Requirements:
pip install matplotlib numpy
If you plan to use the R script:

📊 R Requirements:
R Base
tidyverse (or dplyr, ggplot2 depending on future expansions)

🎮 Features
🌠 Real-time black hole background with parallax animation
🌀 Mouse-controlled lens distortion and magnetic warp field
⚛️ Orbiting particles simulate gravitational light bending
📜 Scrollable research documentation (Pages 1–3 of experiment design)
🎧 Narration player with Starfleet-style UI
🎯 Responsive layout with mobile support and touch lens control

🔧 Dev Notes
To edit styles: all CSS is currently inline inside <head> for simplicity. For modular design, extract to style.css.
To add theory expansions:
Place additional text in #doc-text inside .doc-section
Use <h3>, <p>, or custom diagram blocks like:
<pre> ASCII or logic diagrams here </pre>

🛡 License
MIT License — © 2025 Newport River Company
Open Source Science for Humanity | May your vacuum chamber stay cold, your detectors sensitive, and your lens forever gravitational.

👽 Credits
Simulation & Research Concept: Mark Anthony Bartholomew
AI Code and Interface: (The Architect)
Graphics & Visualization: You, the Explorer

🖖 “To boldly go where no particle has ever interacted.”

