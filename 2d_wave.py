import numpy as np
import matplotlib.pyplot as plt
import landaubeta as hasperdido

hasperdido.use_latex_fonts()

# --- Configuration ---
grid_size = 400        # Resolution of the plot
width = 20.0           # Physical width of the domain
height = 10.0          # Physical height of the domain
wavelength = 0.5       # Wavelength
k = 2 * np.pi / wavelength
slit_dist = 1.5        # Distance between the two slits
slit_x = 4.0           # X-coordinate where the wall/slits are located

# Create the coordinate grid
x = np.linspace(0, width, grid_size)
y = np.linspace(0, height, grid_size)
X, Y = np.meshgrid(x, y)

def calculate_wave():
    # 1. Before the Slit: Simulate a Plane Wave
    # Traveling in the +x direction: psi = cos(kx)
    wave_before = np.cos(k * X)
    
    # 2. After the Slit: Simulate Interference from two point sources
    # Slit positions
    s1_y, s2_y = height/2 - slit_dist/2, height/2 + slit_dist/2
    
    # Distance from each slit to every point in the grid
    r1 = np.sqrt((X - slit_x)**2 + (Y - s1_y)**2)
    r2 = np.sqrt((X - slit_x)**2 + (Y - s2_y)**2)
    
    # Interference pattern (Superposition of two circular waves)
    # We add a small constant to r to avoid division by zero at the source
    wave_after = (np.cos(k * r1) / np.sqrt(r1 + 0.1)) + (np.cos(k * r2) / np.sqrt(r2 + 0.1))
    
    # 3. Combine the two regions
    # Use a mask to show plane waves for x < slit_x and interference for x >= slit_x
    total_wave = np.where(X < slit_x, wave_before, wave_after)
    
    return total_wave

# Generate the wave data
wave_field = calculate_wave()

# --- Plotting ---
plt.figure(figsize=(6, 3))
plt.imshow(wave_field, extent=[0, width, 0, height], origin='lower', 
           cmap='seismic', interpolation='bilinear', vmin=-1.5, vmax=1.5)

# Visualizing the barrier
# plt.axvline(x=slit_x, color='black', linestyle='--', alpha=0.7, label='Slit Barrier')
# plt.scatter([slit_x, slit_x], [width/2 - slit_dist/2, width/2 + slit_dist/2], 
#             color='yellow', s=50, zorder=5, label='Slits')

# plt.colorbar(label='Amplitude')
# plt.title('2D Double Slit Diffraction Simulation')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend(loc='upper right')
plt.xticks([])
plt.yticks([])
plt.show()