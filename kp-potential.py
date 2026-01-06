import numpy as np
import matplotlib.pyplot as plt
from landaubeta import use_latex_fonts, use_IEEE_style
# use_latex_fonts()
use_IEEE_style()

def plot_kp_vs_coulomb():
    num_atoms = 5
    lattice_const = 20.0  # Increased spacing between nuclei
    
    # Grid for plotting
    x = np.linspace(-2, (num_atoms - 1) * lattice_const + 2, 5000)
    
    # 1. Realistic Potential (Coulomb-like: -1/|x|)
    # We drop the softening parameter. To avoid division by zero during 
    # calculation, we use a tiny clipping value (1e-3).
    v_real = np.zeros_like(x)
    for i in range(num_atoms):
        center = i * lattice_const
        dist = np.abs(x - center)
        # The potential goes to -infinity at the center
        v_real -= 1.0 / np.maximum(dist, 1e-3)

    # 2. Kronig-Penney Approximation
    # Making the 'step' negative (wells) and increasing its dimensions
    well_width = 1  # Wider steps
    v0 = -20.0         # Deeper negative potential
    
    v_kp = np.zeros_like(x)
    for i in range(num_atoms):
        center = i * lattice_const
        # Define the rectangular well bounds
        well_start = center - well_width / 2
        well_end = center + well_width / 2
        v_kp = np.where((x >= well_start) & (x <= well_end), v0, v_kp)

    # Plotting
    plt.figure(figsize=(12, 6))
    
    # Plotting Realistic Potential
    plt.plot(x, v_real, label=r"Realistic Potential ($-1/|x|$)", color='royalblue', lw=1.5)
    
    # Plotting K-P Approximation (Step/Rectangular Wells)
    plt.step(x, v_kp, label="Kronig-Penney (Negative Wells)", color='crimson', 
             where='mid', lw=2.5, alpha=0.9)

    plt.title("Atomic Potential vs. Kronig-Penney Model (Negative Wells)", fontsize=14)
    plt.xlabel("Position ($x$)", fontsize=12)
    plt.ylabel("Potential Energy $V(x)$", fontsize=12)
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    
    # Set y-limit to focus on the structure of the wells
    plt.ylim(-10, 1)
    plt.legend(loc='lower right')
    plt.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_kp_vs_coulomb()