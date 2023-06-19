import numpy as np

def diagonalize_matrix(A):
    # Calcula los eigenvalores y eigenvectores
    eigenvalues, eigenvectors = np.linalg.eig(A)
    
    # Construye la matriz diagonal D
    D = np.diag(eigenvalues)
    
    # Construye la matriz P utilizando los eigenvectores como columnas
    P = eigenvectors
    
    # Calcula la matriz inversa de P
    P_inv = np.linalg.inv(P)
    
    # Calcula la matriz diagonalizada A_d
    A_d = np.dot(np.dot(P, D), P_inv)
    
    return A_d, P, D

# Ejemplo de uso
A = np.array([[4, -2], [-2, 1]])
A_d, P, D = diagonalize_matrix(A)

print("Matriz diagonalizada A_d:")
print(A_d)

print("Matriz P:")
print(P)

print("Matriz D:")
print(D)