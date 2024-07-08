import numpy as np
import matplotlib.pyplot as plt

# Parameters for the solar cell
Isc = 5  # Short-circuit current (A)
Voc = 0.6  # Open-circuit voltage (V)
n = 1.3  # Ideality factor
T = 300  # Temperature (K)
k = 1.38e-23  # Boltzmann constant (J/K)
q = 1.6e-19  # Electron charge (C)

# Number of points in the I-V curve
points = 100

# Calculate the thermal voltage
Vt = n * k * T / q

# Voltage array
V = np.linspace(0, Voc, points)

# I-V curve without shading (Shockley diode equation)
I_no_shading = Isc * (1 - np.exp(V / Vt - 1))

# Partial shading effect (50% shading on half of the cell)
shaded_factor = 0.5
Isc_shaded = Isc * shaded_factor

# I-V curve with partial shading
I_with_shading = np.concatenate([Isc * (1 - np.exp(V[:points//2] / Vt - 1)),
                                 Isc_shaded * (1 - np.exp(V[points//2:] / Vt - 1))])

# Plotting the I-V curves
plt.figure(figsize=(10, 6))
plt.plot(V, I_no_shading, label='Without Shading')
plt.plot(V, I_with_shading, label='With Partial Shading', linestyle='--')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (I)')
plt.title('I-V Characteristics of Solar Cell with and without Partial Shading')
plt.legend()
plt.grid(True)
plt.show()
