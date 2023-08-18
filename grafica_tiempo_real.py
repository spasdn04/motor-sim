import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as rd
import time
import keyboard

#Generamos datos aleatorios para graficarlos
fig, ax = plt.subplots()
t = [1, 1]
c = 1
c1 = 1
data = [1000, 1000]
while True:
    time.sleep(0.001)
    if len(t) == 15:
        t = np.delete(t, 0)
        t = np.append(t, t[-1] + c)
        data = np.delete(data, 0)
        data = np.append(data, np.random.randint(800, 1000))
    else:
        c1 += 1
        t = np.append(t, c1)
        data = np.append(data, np.random.randint(800, 1000))
    
    print(data, t)

    plt.cla()
    ax.plot(t, data ,'r')
    plt.pause(0.001)

    if keyboard.is_pressed('q') == True:
        break