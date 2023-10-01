import matplotlib.pyplot as plt
import numpy as np

values1 = np.random.normal(0, 10, 1000)

values3 = np.random.normal(0, 10, 3000)/3
fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.hist(values1, 200)
ax2.hist(values3, 200)

plt.show()
