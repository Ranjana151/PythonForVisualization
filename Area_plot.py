import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame(np.random.rand(10, 4), columns=["a", "b", "c", "d"])
plt.style.use("dark_background")
df.plot.area(stacked=True, color=["red", "green", "yellow", "blue"])
plt.show()
