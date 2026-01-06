import numpy as np
import matplotlib.pyplot as plt
import landaubeta as lb

lb.use_latex_fonts()

# --- Physical Parameters ---
wavelength = 0.2e-3  # 0.2 mm
L = 1.0              # 1 meter
d = 0.01             # 10 mm separation
a = 0.002            # 2 mm slit width

# Screen coordinates
x = np.linspace(-0.06, 0.06, 5000)
theta = np.arctan(x/L)

# --- 1. Calculate Wave Intensity ---
alpha = (np.pi * d * np.sin(theta)) / wavelength
beta = (np.pi * a * np.sin(theta)) / wavelength
wave_intensity = (np.sinc(beta/np.pi)**2) * (np.cos(alpha)**2)

# Normalize to get PDF (in meters^-1)
area_wave = np.trapz(wave_intensity, x)
pdf_m = wave_intensity / area_wave

# --- 2. Generate Random Samples ---
# Probabilities for np.random.choice must sum to 1
p_choice = pdf_m / np.sum(pdf_m)
n_samples = 5000
samples_m = np.random.choice(x, size=n_samples, p=p_choice)

# --- 3. Convert to mm for plotting ---
x_mm = x * 1000
pdf_mm = pdf_m / 1000  # Convert density to mm^-1
samples_mm = samples_m * 1000

# --- Plotting ---
plt.figure(figsize=(6, 3))

# Plot Theoretical Wave
plt.plot(x_mm, pdf_mm, linewidth=1.5, label=r"$|\psi|^2$")

# Plot Histogram (density=True ensures area under histogram is 1)
plt.hist(samples_mm, bins=150, density=True, alpha=0.5, label='Electron detections')

plt.xlabel("Position on Screen", fontsize=12)
plt.ylabel("Electron counts (normalized)", fontsize=12)
plt.legend(loc='upper right')
plt.xticks([])
plt.yticks([])
plt.xlim(-50, 50)
plt.tight_layout()
plt.show()
