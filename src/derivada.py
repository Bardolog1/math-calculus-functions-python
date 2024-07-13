import numpy as np
import matplotlib.pyplot as plt

# Definir constantes
a = 5
x0 = 4

# Definir las funciones
def f1(x):
    return (2 - a * x) / (a + 2)

def f2(x):
    return (1 / (1 + a)) * np.log(x + 1 / 3)

# Derivadas de las funciones
def f1_prime(x):
    return -a / (a + 2)

def f2_prime(x):
    return 1 / (6 * (x + 1 / 3))

# Evaluación de las funciones en x0
f1_x0 = f1(x0)
f2_x0 = f2(x0)

# Pendientes en x0
m1 = f1_prime(x0)
m2 = f2_prime(x0)

# Ecuaciones de las rectas tangentes
def tangent1(x):
    return m1 * (x - x0) + f1_x0

def tangent2(x):
    return m2 * (x - x0) + f2_x0

# Valores de x para graficar
x_vals = np.linspace(0, 8, 400)

# Graficar f(x) y la recta tangente para la primera función
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(x_vals, f1(x_vals), label="f(x) = (2 - 5x) / 7")
plt.plot(x_vals, tangent1(x_vals), '--', label="Tangente en x = 4")
plt.scatter([x0], [f1_x0], color='red') # Punto (4, f(4))
plt.title("Función 1 y su Recta Tangente")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

# Graficar f(x) y la recta tangente para la segunda función
plt.subplot(1, 2, 2)
plt.plot(x_vals, f2(x_vals), label="f(x) = ln(x + 1/3) / 6")
plt.plot(x_vals, tangent2(x_vals), '--', label="Tangente en x = 4")
plt.scatter([x0], [f2_x0], color='red') # Punto (4, f(4))
plt.title("Función 2 y su Recta Tangente")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

plt.tight_layout()
plt.show()
