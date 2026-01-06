import numpy as np
import matplotlib.pyplot as plt
import landaubeta as lb

lb.use_latex_fonts()

# --- Physical Parameters ---
wavelength = 0.2e-3  # 0.2 mm
L = 1.0              # 1 meter
d = 0.01             # 10 mm separation
a = 0.002            # 2 mm slit width
sigma = 0.003        # 3 mm spread for particles

# Screen coordinates
x = np.linspace(-0.06, 0.06, 3000)
theta = np.arctan(x/L)

# --- 1. Calculate Wave Intensity ---
alpha = (np.pi * d * np.sin(theta)) / wavelength
beta = (np.pi * a * np.sin(theta)) / wavelength
wave_intensity = (np.sinc(beta/np.pi)**2) * (np.cos(alpha)**2)

# --- 2. Calculate Particle Intensity ---
p1 = np.exp(-(x - d/2)**2 / (2 * sigma**2))
p2 = np.exp(-(x + d/2)**2 / (2 * sigma**2))
particle_intensity = p1 + p2

# --- 3. Area Normalization ---
# Compute the area under each curve using the trapezoidal rule
area_wave = np.trapz(wave_intensity, x)
area_particle = np.trapz(particle_intensity, x)

# Normalize so that the integral of each is 1.0
wave_norm = wave_intensity / area_wave
particle_norm = particle_intensity / area_particle

# --- Plotting ---
plt.figure(figsize=(6, 3))
plt.plot(x * 1000, wave_norm, label='Wave Model')
plt.plot(x * 1000, particle_norm, label='Particle Model', linestyle='--')

# plt.title("Double Slit Pattern: Area-Normalized Wave vs. Particle Theory", fontsize=14)
plt.xlabel("Position on Screen", fontsize=12)
plt.ylabel("Probability Density", fontsize=12)
plt.legend()
# plt.grid(True, linestyle=':', alpha=0.6)
plt.xticks([])
plt.yticks([])
plt.xlim(-50, 50)
plt.tight_layout()
plt.show()