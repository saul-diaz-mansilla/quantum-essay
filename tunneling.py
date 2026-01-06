import numpy as np
import matplotlib.pyplot as plt
import landaubeta as lb
lb.use_latex_fonts()

# Parameters for the barrier
barrier_pos = 0.0
barrier_width = 0.2  # Very thin barrier
barrier_height = 100.0 # Tall barrier

# Parameters for the wave
k = 2 * np.pi # Wave number
x = np.linspace(-5, 5, 10000)

# Incident wave (real part of e^(ikx))
incident_wave = 5 * np.cos(k * x[x < -0.2]) + 50

# Create the barrier potential
potential = np.zeros_like(x)
potential[(x > barrier_pos - barrier_width/2) & (x < barrier_pos + barrier_width/2)] = barrier_height

# Plotting
plt.figure(figsize=(6, 4))

# Plot the potential barrier
plt.plot(x, potential, 'r', linewidth=2, label='Potential Barrier')
plt.fill_between(x, 0, potential, color='red', alpha=0.3)

# Plot the incident wave
plt.plot(x[x < -0.2], incident_wave, 'b--', label='Incident Wave')

# Add text box for b -> 0
# plt.text(0.95, 0.05, r'$b \to 0, bV_0=\beta$', transform=plt.gca().transAxes,
#          fontsize=16, verticalalignment='bottom', horizontalalignment='right',
#          bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5))

# plt.title('Incident Wave on a Thin, Tall Potential Barrier')
plt.xlabel('Position (x)')
plt.ylabel('Amplitude / Potential')
locs, labels = plt.xticks([-barrier_width/2, barrier_width/2], [r'$-b/2$', r'$b/2$'])
labels[0].set_horizontalalignment('right')
labels[1].set_horizontalalignment('left')
plt.yticks([barrier_height, barrier_height/2], [r'$V_0$', r"$E$"])
plt.ylim(-1.5, barrier_height + 10) # Adjust y-limit to show both wave and barrier
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()
