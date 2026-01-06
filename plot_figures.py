import numpy as np
import matplotlib.pyplot as plt
import landaubeta as hasperdido

hasperdido.use_latex_fonts()

m = 9.1093837e-31
hbar = 1.054571817e-34
E = np.linspace(0, 100 * 1.160218e-19, 20000)

a_values = np.array([3.61, 5.43, 5.64]) * 1e-10
b_values = .1 * a_values
V_0_values = - np.array([4.5, 12, 40]) * 1.160218e-19

for a, b, V_0 in zip(a_values, b_values, V_0_values):
	kappa = m * b * V_0 / hbar**2
	q = np.sqrt(2 * m * E) / hbar
	f = np.cos(q * a) + kappa / q * np.sin(q * a)

	fig, ax = plt.subplots(figsize=(4*.7,2.5*.7))
	ax.plot(E / 1.160218e-19, f, label=r"$\cos(ka) + (q/k) \sin(ka)$")
	ax.plot(E / 1.160218e-19, np.ones_like(E), 'r--', label="Limits")
	ax.plot(E / 1.160218e-19, -np.ones_like(E), 'r--')

	# Detect contiguous regions where f is between -1 and 1
	mask = (f >= -1) & (f <= 1)
	if mask.any():
		idx = np.nonzero(mask)[0]
		# find breaks in the index sequence to get contiguous segments
		breaks = np.where(np.diff(idx) > 1)[0]
		starts = idx[np.concatenate(([0], breaks + 1))]
		ends = idx[np.concatenate((breaks, [len(idx) - 1]))]
		for s, e in zip(starts, ends):
			# use the energy values at the segment boundaries for shading
			x0 = E[s] / 1.160218e-19
			x1 = E[e] / 1.160218e-19
			ax.axvspan(x0, x1, color='C0', alpha=0.2, zorder=0)

	ax.set_xlabel('Electron Energy (eV)')
	ax.set_ylabel(r"$\cos(ka) + (q/k) \sin(ka)$")
	ax.set_ylim(-4, 4)
	# ax.legend()
	plt.tight_layout()
	plt.show()