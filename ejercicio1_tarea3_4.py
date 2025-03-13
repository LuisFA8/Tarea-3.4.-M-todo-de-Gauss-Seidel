# -*- coding: utf-8 -*-
"""Ejercicio1_Tarea3.4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j2upiSrgV_kiUMfexyv4dbkVJlEkTuh0
"""

import numpy as np
import matplotlib.pyplot as plt

def gauss_seidel(A, b, tol=1e-6, max_iter=100):
    n = len(b)
    # Valor inicial inicia en 0 por defecto
    x = np.zeros(n)
    x_prev = np.copy(x)
    errors = []

    for k in range(max_iter):
        for i in range(n):
            sum1 = sum(A[i][j] * x[j] for j in range(i))
            sum2 = sum(A[i][j] * x_prev[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum1 - sum2) / A[i][i]

        abs_error = np.linalg.norm(x - x_prev, ord=np.inf)
        rel_error = abs_error / (np.linalg.norm(x, ord=np.inf) + 1e-10)
        quad_error = np.linalg.norm(x - x_prev) ** 2

        errors.append((k, abs_error, rel_error, quad_error))

        if abs_error < tol:
            break

        x_prev = np.copy(x)

    return x, errors

A = np.array([
    [10, 2, 3, 1],
    [2, 12, 2, 3],
    [3, 2, 15, 1],
    [1, 3, 1, 10]])

b = np.array([15, 22, 18, 10])

# Llamada a la función de Gauss-Seidel
x_sol, errors = gauss_seidel(A, b)

# Imprimir errores en formato de tabla
print(f"{'Iteración':<12}{'Error absoluto':<20}{'Error relativo':<20}{'Error cuadrático':<20}")
print("-" * 72)
for k, abs_error, rel_error, quad_error in errors:
    print(f"{k:<12}{abs_error:<20.10e}{rel_error:<20.10e}{quad_error:<20.10e}")

# Imprimir la solución aproximada
print("\nSolución aproximada:")
for i, val in enumerate(x_sol, 1):
    print(f"I{i} = {val:.10e}")


# Graficar errores
iterations = [e[0] for e in errors]
abs_errors = [e[1] for e in errors]
rel_errors = [e[2] for e in errors]
quad_errors = [e[3] for e in errors]

plt.figure(figsize=(10, 5))
plt.plot(iterations, abs_errors, label="Error absoluto", color='blue', linestyle='-', linewidth=2)
plt.plot(iterations, rel_errors, label="Error relativo", color='green', linestyle='--', linewidth=2)
plt.plot(iterations, quad_errors, label="Error cuadrático", color='red', linestyle=':', linewidth=2)
plt.yscale("log")
plt.xlabel("Iteraciones", fontsize=12)
plt.ylabel("Errores", fontsize=12)
plt.title("Convergencia del método de Gauss-Seidel", fontsize=14)
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.savefig("convergencia_gauss_seidel.png")
plt.show()