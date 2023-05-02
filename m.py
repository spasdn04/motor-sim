import numpy as np
import sympy as sp

def QnA(Asa):
    n = Asa.shape[0]
    Qy = 0
    X = sp.symbols(f'x:{n+1}')
    
    # Calculo del polinomio
    for i in range(n-1):
        if Asa[i,i] == 0:
            continue
        inner_sum = 0
        for j in range(i, n):
            inner_sum += (Asa[i,j] / Asa[i,i]) * X[j]
        Qy += ( Asa[i,i] * inner_sum ** 2 )
    
    print(f'la matriz de la forma cuadrática es: \n {Asa}')
    print('El polinomio en forma de cuadrados es:')
    print(f'Q(y) = {Qy}')
    
A = np.random.randint(-4,4,[3,3])
As = A.transpose() + A

QnA(As)    