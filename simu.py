import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants and Parameters
light_intensity = 1000  # Light intensity in W/m²
photon_absorption_efficiency = 0.8  # Efficiency of photon absorption
electron_injection_efficiency = 0.9  # Efficiency of electron injection
electron_transport_time_constant = 0.01  # Time constant for electron transport (s)
regeneration_efficiency = 0.95  # Efficiency of electrolyte regeneration
load_resistance = 1  # Load resistance in Ohms
open_circuit_voltage = 0.7  # Open-circuit voltage in volts

# Model Dynamics
def dssc_dynamics(y, t, light_intensity, photon_absorption_efficiency, electron_injection_efficiency, electron_transport_time_constant):
    n_absorbed_photons = light_intensity * photon_absorption_efficiency
    n_injected_electrons = n_absorbed_photons * electron_injection_efficiency
    
    # y[0] is the transported electrons
    dne_dt = (n_injected_electrons - y[0]) / electron_transport_time_constant
    return [dne_dt]

# Time for simulation
t = np.linspace(0, 10, 1000)  # 10 seconds with 1000 time points

# Initial conditions
y0 = [0]  # Initial transported electrons

# Solve ODE
sol = odeint(dssc_dynamics, y0, t, args=(light_intensity, photon_absorption_efficiency, electron_injection_efficiency, electron_transport_time_constant))

# Extract transported electrons
transported_electrons = sol[:, 0]

# Calculate Current and Voltage
current_density = transported_electrons  # Assuming direct proportionality
current = current_density * regeneration_efficiency  # Current in Amperes
voltage = open_circuit_voltage - (current * load_resistance)  # Voltage in Volts
power = voltage * current  # Power in Watts

# Plotting the results
plt.figure(figsize=(12, 6))

# Current vs Time
plt.subplot(2, 2, 1)
plt.plot(t, current, label='Current', color='b')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.title('Current vs Time')
plt.grid()
plt.legend()

# Voltage vs Time
plt.subplot(2, 2, 2)
plt.plot(t, voltage, label='Voltage', color='r')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Voltage vs Time')
plt.grid()
plt.legend()

# Current vs Voltage
plt.subplot(2, 2, 3)
plt.plot(voltage, current, label='I-V Curve', color='g')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.title('Current vs Voltage')
plt.grid()
plt.legend()

# Power vs Voltage
plt.subplot(2, 2, 4)
plt.plot(voltage, power, label='P-V Curve', color='m')
plt.xlabel('Voltage (V)')
plt.ylabel('Power (W)')
plt.title('Power vs Voltage')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
