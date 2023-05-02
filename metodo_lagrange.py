import numpy as np
import math as mt
"""
A1 = np.array([[1,2,1],[2,1,1],[1,1,3]])
A2 = A1.transpose()
A=A1+A2
print('La matriz A de 3x3 simétrica es:\n')
print(A1)
[[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]] = A1

b11 = a11 + 2 * mt.sqrt(a11 * a12 * a13 / (a22 * a33) + a12**2 / a22 + a13**2 / a33) + a22 / 2 + a33 / 2
b12 = (a22 - a33 + mt.sqrt((a33 - a22)**2 + 4 * a12**2)) / 2
b21 = (a22 - a33 + mt.sqrt((a33 - a22)**2 + 4 * a12**2)) / 2
b13 = (a22 + a33 - b12) / 2
b31 = (a22 + a33 - b12) / 2
b22 = a11 - 2 * mt.sqrt(a11 * a12 * a13 / (a22 * a33) + a12**2 / a22 + a13**2 / a33) + a22 / 2 + a33 / 2
b23 = (a23 / mt.sqrt(a22)) * (b22 - a33) / a23
b32 = (a23 / mt.sqrt(a22)) * (b22 - a33) / a23
b33 = a11 - b12 - b13 - b22

B = [[b11,b12,b13],[b21,b22,b23],[b31,b32,b33]]

print(B)"""

print('--------------------------------------------------------------------------------------------------------------------')

import numpy as np
from scipy.linalg import eig

def diagonalize_quadratic_form(A):
    # Paso 1: diagonalizar la matriz simétrica A
    eigvals, eigvecs = eig(A)
    P = eigvecs.transpose()
    
    # Paso 2: transformar las variables y obtener la forma cuadrática diagonal
    D = np.diag(eigvals)
    Q = lambda y: np.dot(y.transpose(), np.dot(D, y))
    
    return P, Q, D

A = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 4]])
P, Q, D = diagonalize_quadratic_form(A)

print('D: \n', D)
print("P: \n", P)
print("Q(y): ", Q(np.array([1,1,4])))