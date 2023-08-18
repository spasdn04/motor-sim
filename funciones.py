import numpy as np
import matplotlib.pyplot as plt
import time

# ---------------- gráfica dinámica para mostrar los disintos parámetros en tiempo real

f = 10
T = 1 / 10

t  =np.linspace(0, 5*T, 3*100)
diff = t[1] - t[0]

s1 = t * 1.5
s2 = 1*np.sin(2 * np.pi * f * t)
s3 = 2 * np.exp(-2 * t) * np.sin(2 * np.pi * 5 * f * t)

fig, ax = plt.subplots()


if __name__ == '__main__':
    while True:
        t = np.delete(t, 0)
        t = np.append(t, t[-1]+ diff)
        
        s1 = t * 1.5
        s2 = 1 * np.sin(2 * np.pi * f * t)
        s3 = 2 * np.exp(-2 * t) * np.sin(2 * np.pi * 5 * f * t)
        
        plt.cla()
        ax.plot(t, s1, 'r', t, s2, 'g', t, s3, 'b')
        plt.pause(0.001)