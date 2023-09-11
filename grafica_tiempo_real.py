import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as rd
import time, keyboard

#Generamos datos aleatorios para graficarlos, y hacemos que la lista se mueva 15 posiciones eliminando las primeras que estaban
fig, ax = plt.subplots()
t = [1, 1]
c = 0.1
c1 = 0.1
data = [1000, 1000]
start_time = time.perf_counter()
graph = []

while True:
    if len(t) == 15:
        t = np.delete(t, 0)
        t = np.append(t, t[-1] + c)
        data = np.delete(data, 0)
        if t[-1] >= 10:
            data = np.append(data, np.random.randint(1800, 2000))
            graph = np.append(graph, data[-1])
        else:
            data = np.append(data, np.random.randint(800, 1000))
            graph = np.append(graph, data[-1])
    else:
        t = np.append(t, t[-1] + c1)
        data = np.append(data, np.random.randint(800, 1000))
        graph = np.append(graph, data[-1])
    
    #print(data, t)
    
    plt.cla()
    ax.plot(t, data ,'r')
    plt.title('Revoluciones')
    ax.legend(['rpm'])
    plt.xlabel('Tiempo (ds)')
    plt.ylabel('rpm')
    plt.ylim(0,2000)
    plt.pause(0.1)

    # Detenemos el bucle con el teclado
    if keyboard.is_pressed('q') == True:
        end_time = time.perf_counter()
        plt.close()
        break

#Calculamos el tiempo de ejecución
execution_time = end_time - start_time 
print(f"tiempo del ciclo: {execution_time: .5f} segundos")
T = np.linspace(1, len(graph), len(graph))
print(T)
figure, ax = plt.subplots()
ax.plot(T, graph, 'g')
plt.show()