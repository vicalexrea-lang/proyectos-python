import numpy as np

# Corrección del diagnóstico
I = np.array([[1, 0],
              [0, 1]])
B = np.array([[5, 3],
              [2, 7]])

print("I × B =\n", I @ B)   # debe dar exactamente B

# Transformación de escala
A = np.array([[2, 0],
              [0, 2]])
v = np.array([3, 1])
print("\nEscala × v =", A @ v)   # [6, 2]

# Rotación 90°
R = np.array([[0, -1],
              [1,  0]])
print("Rotar v =", R @ v)   # [-1, 3]
