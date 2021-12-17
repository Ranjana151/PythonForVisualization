import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.DataFrame(np.random.rand(10, 5))
plt.style.use("dark_background")
color = {
    "boxes": "DarkGreen",
    "whiskers": "DarkOrange",
    "medians": "DarkBlue",
    "caps": "red",
}

data.plot.box(color=color)
plt.title("Box Plot", color="blue", fontsize=50)
plt.show()
