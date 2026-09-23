import numpy as np
a = np.linspace(-np.pi, np.pi, 100)
b = np.cos(a)
c = np.sin(a)
d = b@c
print(d)