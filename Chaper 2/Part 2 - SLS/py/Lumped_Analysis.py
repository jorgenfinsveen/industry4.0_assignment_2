import math

T = 333.15      # Kelvin / 60 Celsius
Ta = 298.15     # Kelvin / 25 Celsius
Ti = 434.00     # Kelvin
h = 10          # W/(m^2*K)
A = 0.17193     # m^2
V = 0.0039687   # m^3
p = 525         # kg/m^3
Cp = 3000       # J/kg*K

def cooling_time():
    eq1 = -Cp * V * p
    eq2 = (T - Ta) / (Ti - Ta)
    eq3 = A * h

    seconds = eq1 * (math.log(eq2) / eq3)
    hours = seconds / (60 * 60)

    return seconds, hours

print(cooling_time())






