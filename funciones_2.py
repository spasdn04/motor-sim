import numpy as np
import matplotlib.pyplot as plt
import time

# -------------------------------- Gráfica dinámica para mostrar los disintos parámetros en tiempo real. ----------------------------------------------------

I = np.array([0.0147, 0.0157, 0.0167, 0.0177, 0.0187, 0.0197, 0.0207, 0.0217, 0.0227])
Vi = np.array([0.566, 0.546])

fig, ax = plt.subplots()
ax.legend()
ax.plot(I, Vi)

if __name__ == '__main__':
    plt.show()