import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,1)
y=np.sin(4* np.pi * x)

plt.fill(x,y)
plt.show()

