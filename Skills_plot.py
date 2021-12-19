import numpy as np
import matplotlib.pyplot as plt

python = (70, 65, 70, 80)
machine_learning = (80, 90, 95, 78)
dataStructure = (95, 78, 56, 80)
aws = (50, 70, 90, 76)
person = ["Ranjana", "Sonal", "Abhishek", "Sangam"]

plt.style.use('dark_background')
index = np.arange(4)
plt.bar(index, python, width=0.2, label="Python", color="red")
plt.bar(index + 0.2, machine_learning, width=0.2, label="Machine Learning", color="green")
plt.bar(index + 0.4, dataStructure, width=0.2, label="Data Structure", color="blue")
plt.bar(index + 0.6, aws, width=0.2, label="Aws", color="yellow")
plt.xlabel("Persons", fontsize=25)
plt.ylabel("Skill Level", fontsize=25)
plt.title("IT Skill Levels", fontsize=45, color="yellow")
plt.xticks(index + 0.2, person, color="blue", fontsize=15)
plt.legend(loc="upper left")
plt.ylim(0, 100)
plt.show()
