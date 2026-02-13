# quantum-essay
An essay about basic concepts of quantum mechanics explained at the level of a 1st year physics student. Topics include wavefunctions, quantum tunneling, and a simple model of conductivity (Kronig-Penney model).

Figures were made using Python with the assistance of GAI for rapid script prototyping. The essay and models were inspired by derivations from the PLANCKS competition and standard texts like Griffiths' Introduction to Quantum Mechanics and the Feynman Lectures.

Read final essay in "Essay.pdf".
Description of the assignment and tasks in "Quantum_Essay_Assignment.pdf".

Folders:
- Sources: References and useful sources cited in the essay.
- latex: Latex files for compiling the main essay document.

Useful functions:
- "landaubeta.py": General utility functions for formatting and numerical analysis.

Main analysis:
Section 2: The wavefunction: why probabilities?
- "2d_wave.py": Generates the visualization of interference resulting from light passing through two slits.
- "interference_pattern.py": Plots the interference pattern comparing the wave model behavior and the classical particle model behavior.
- "interference_histogram.py": Plots the histogram of electron detections on a screen to match the interference pattern predicted by wave mechanics.

Section 4: Quantum tunneling: when intuition fails
- "tunneling.py": Script used to calculate and analyze the quantum tunneling probabilities.

Section 5: Quantum crystals and semiconductors
- "kp-potential.py": Visualizes the Kronig-Penney approximation for the potential of a 1D solid using delta functions.
- "bands.py": Computes and plots the allowed conduction bands and forbidden gaps of Cu, NaCl, and Si.
- "bands_wide.py": Wide  version of the previous one.