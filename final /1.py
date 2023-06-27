from math import exp, log

x1 = 0.1
y1 = (exp(x1)) / (2 * log(3 * pow(x1, 2)))

print(f"Значення e^x / (2*ln(3x^2) при х = {x1}: {y1}")

x2 = 0.624
y2 = pow(x2, 5) + pow(x2, 4) + 4.2 * pow(x2, 3) + 5.3 * pow(x2, 2) + 6.4 * x2 + 7.5

print(f"Значення x^5 + x^4 + 4.2x^3 + 5.3x^2 + 6.4x + 7.5 при значенні x = {x2}: {y2}")