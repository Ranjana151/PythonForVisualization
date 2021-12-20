import matplotlib.pyplot as plt

Nations = ["Indian", "American", "French", "Germany"]
Student = [50, 80, 250, 170]
color = ["red", "green", "blue", "brown"]
explode = [0.1, 0, 0, 0]
pair = zip(Student, Nations)
pair = sorted(list(pair))
Student, Nations = zip(*pair)
plt.style.use("dark_background")
plt.pie(Student, labels=Nations, colors=color, autopct="%.2f%%", counterclock=False, startangle=90, explode=explode,
        wedgeprops={'linewidth': 2.0, 'edgecolor': 'white'})
plt.title("Students Nationality", fontsize=50, color="blue")
plt.show()
