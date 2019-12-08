import matplotlib.pyplot as plot
import numpy as np

f = np.arange(0,99)
for n in range(99):
    if n<=9:
        f[n] = (f[n]**2) - 7
    else:
        f[n] = f[n - 10]
plot.stem(f,use_line_collection=True)
plot.show()