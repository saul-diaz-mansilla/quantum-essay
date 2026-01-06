import numpy as np
import matplotlib.pyplot as plt

def plot_delta_limit(strength=1.0, iterations=5):
    """
    Plots a series of barrier potentials tending towards a delta function.
    
    Parameters:
    strength: The area under the curve (V0 * a)
    iterations: Number of steps to show the narrowing process
    """
    x = np.linspace(-2, 2, 1000)
    plt.figure(figsize=(10, 6))
    
    # Colors for visual clarity
    colors = plt.cm.viridis(np.linspace(0, 1, iterations))

    for i in range(iterations):
        # As width 'a' decreases, height 'V0' increases proportionally
        a = 1.0 / (2**i) 
        v0 = strength / a
        
        # Define the rectangular barrier
        # Potential is v0 if |x| < a/2, else 0
        y = np.where(np.abs(x) <= a/2, v0, 0)
        
        label = f'Width $a={a:.3f}$, Height $V_0={v0:.1f}$'
        plt.plot(x, y, label=label, color=colors[i], lw=2)
        plt.fill_between(x, y, alpha=0.1, color=colors[i])

    plt.title(f"Barrier Potential Tending to a Delta Function (Area = {strength})", fontsize=14)
    plt.xlabel("Position (x)", fontsize=12)
    plt.ylabel("Potential $V(x)$", fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.ylim(0, v0 + 1) # Adjust y-limit to the tallest barrier
    plt.show()

if __name__ == "__main__":
    plot_delta_limit(strength=1.0, iterations=6)