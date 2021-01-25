import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1890, 1892, 1897, 1902, 1907, 1912, 1917, 1922])
ypoints = np.array([16000, 2000, 4000, 6000, 1000, 5000, 0, 16000])

plt.plot(xpoints, ypoints)
plt.show()