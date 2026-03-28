import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 0, -1])

# Producto punto — tres formas de calcularlo, todas dan lo mismo
print(np.dot(a, b))       # forma estándar
print(a @ b)              # operador @ — el más usado en ML
print(sum(a[i]*b[i] for i in range(len(a))))  # manual, para entender

# Resultado: 1*4 + 2*0 + 3*(-1) = 4 + 0 - 3 = 1