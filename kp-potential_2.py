import numpy as np
import matplotlib.pyplot as plt
from landaubeta import use_latex_fonts, use_IEEE_style
use_latex_fonts()

def plot_final_diagram_with_arrows():
    num_atoms = 5
    a_dist = 20.0  
    x = np.linspace(-1, (num_atoms - 1) * a_dist + 2, 3000)
    
    # 1. Potentials
    v_real = np.zeros_like(x)
    v_kp = np.zeros_like(x)
    well_width, v0 = 1.0, -20.0
    for i in range(num_atoms):
        center = i * a_dist
        v_real -= 1.8 / np.maximum(np.abs(x - center), 0.15)
        v_kp = np.where(np.abs(x - center) <= well_width/2, v0, v_kp)

    fig, ax = plt.subplots(figsize=(9, 4.5))
    
    # Plotting lines
    ax.plot(x, v_real, color='#1f77b4', lw=2, label="Atomic Potential")
    ax.plot(x, v_kp, color='#d62728', lw=2.5, label="Kronig-Penney")

    # --- AXES STYLING ---
    # Move X-axis to zero
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position(('data', -1)) # Set Y-axis at the start of plot
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Add Arrow at the end of X-axis
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    # Add Arrow at the end of Y-axis
    ax.plot(-1, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

    # Label Positioning
    ax.text(1.03, 0, '$x$', transform=ax.get_yaxis_transform(), 
            ha='left', va='center', fontsize=14, fontweight='bold')
    ax.text(-1, 1.05, '$V(x)$', transform=ax.get_xaxis_transform(), 
            ha='center', va='bottom', fontsize=14, fontweight='bold')

    # Ticks on top of the x-axis line
    ticks = [i * a_dist for i in range(num_atoms)]
    ax.set_xticks(ticks)
    ax.set_xticklabels(['0'] + [f'${i}a$' for i in range(1, num_atoms)], fontsize=14)
    ax.tick_params(axis='x', pad=-25) 
    ax.set_yticks([]) # Hide Y numbers
    
    plt.ylim(-10, 2)
    plt.legend(loc='lower right')
    plt.show()

plot_final_diagram_with_arrows()