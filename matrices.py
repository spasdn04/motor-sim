from numpy import matrix

a = matrix('4, -2; -2, 1')
print(a)

n = a.shape[0]
print(n)

def Gauss(a):
    #Definimos la dimension de la matriz
    n = a.shape[0]
    for i in range(n):
        max = a[i,i]
        print(f'max element in file {i} is: {max}')
        
        # Hacemos pivoteo parcial cambiando las filas
        for j in range(n):
            c = a[j,i]
            if c >= max:
                b = a[i,:]
                a[i,:] = a[j,:]
                a[j,:] = b
        
        #Hacemos debajo de la diagonal
        for k in range(i+1,n):
            fac = - (a[k,i] / a[i,i])
            print(f'fac: {fac}')
            a[k,:] = a[k,:] + fac*a[i,:]
        print(a)
        
        
Gauss(a)