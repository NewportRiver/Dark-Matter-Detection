# casimir_shift_analysis.R
# Starfleet Casimir Anomaly Detector
# Analyze spectral noise between plates for anomalies caused by dark matter presence

# --- Casimir Force Model ---
casimir_force <- function(a) {
  hbar <- 1.055e-34  # Planck constant / 2pi
  c <- 3.0e8         # Speed of light (m/s)
  return((pi^2 * hbar * c) / (240 * a^4))  # Force per unit area
}

# Simulated plate distances (nm to m)
distances <- seq(1e-9, 1e-7, length.out = 200)
forces <- casimir_force(distances)

# Simulated anomaly (hypothetical dark matter interaction zone)
anomaly_zone <- c(80, 100)
forces[anomaly_zone[1]:anomaly_zone[2]] <- forces[anomaly_zone[1]:anomaly_zone[2]] * 0.95

# Plot the result
plot(distances * 1e9, forces * 1e6, type = 'l', col = 'cyan', lwd = 2,
     xlab = "Plate Distance (nm)", ylab = "Casimir Force (uN/m^2)",
     main = "Simulated Casimir Force with Quantum Vacuum Anomaly")

# Highlight anomaly
abline(v = distances[anomaly_zone[1]] * 1e9, col = "magenta", lty = 2)
abline(v = distances[anomaly_zone[2]] * 1e9, col = "magenta", lty = 2)
legend("topright", legend = c("Normal Force", "Anomaly Zone"),
       col = c("cyan", "magenta"), lty = c(1, 2), lwd = 2)

grid()
