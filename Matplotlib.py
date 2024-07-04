# 1. Installation
# To install Matplotlib, you can use pip:


pip install matplotlib

# 2. Basic Plotting
# 2.1. Importing Matplotlib

import matplotlib.pyplot as plt
# 2.2. Simple Line Plot
python
Copy code
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Simple Line Plot')
plt.show()

# 3. Customizing Plots
# 3.1. Line Style and Color

plt.plot(x, y, color='green', linestyle='--', linewidth=2)
plt.show()

# 3.2. Markers

plt.plot(x, y, marker='o', color='blue')
plt.show()

# 3.3. Adding Grid

plt.plot(x, y)
plt.grid(True)
plt.show()

# 4. Subplots
# 4.1. Simple Subplot

fig, axs = plt.subplots(2)

axs[0].plot(x, y, color='red')
axs[1].plot(y, x, color='blue')

plt.show()

# 4.2. Subplot with Grid

fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(x, y, color='red')
axs[0, 1].plot(y, x, color='blue')
axs[1, 0].plot(x, [i*2 for i in y], color='green')
axs[1, 1].plot(y, [i*2 for i in x], color='purple')

plt.show()

# 5. Bar Charts
# 5.1. Simple Bar Chart

categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

plt.bar(categories, values)
plt.show()

# 5.2. Horizontal Bar Chart

plt.barh(categories, values)
plt.show()

# 6. Histograms
# 6.1. Simple Histogram

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

plt.hist(data, bins=4)
plt.show()

# 7. Scatter Plots
# 7.1. Simple Scatter Plot

plt.scatter(x, y)
plt.show()

# 7.2. Scatter Plot with Color and Size

colors = [10, 20, 30, 40, 50]
sizes = [100, 200, 300, 400, 500]

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)
plt.show()

# 8. Pie Charts
# 8.1. Simple Pie Chart

labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

plt.pie(sizes, labels=labels)
plt.show()

# 8.2. Pie Chart with Explode

explode = (0.1, 0, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=140)
plt.show()

# 9. Advanced Features
# 9.1. Annotations

plt.plot(x, y)
plt.annotate('Peak', xy=(5, 11), xytext=(3, 10),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()

# 9.2. Logarithmic Scale

plt.plot(x, y)
plt.yscale('log')
plt.show()

# 9.3. Multiple Plots in One Figure

plt.figure()

plt.subplot(2, 1, 1)
plt.plot(x, y, 'o-')
plt.title('Subplot 1')

plt.subplot(2, 1, 2)
plt.plot(y, x, '.-')
plt.title('Subplot 2')

plt.tight_layout()
plt.show()

# 9.4. Saving Figures

plt.plot(x, y)
plt.savefig('my_plot.png')
plt.show()

# 9.5. Interactive Mode

plt.ion()
plt.plot(x, y)
plt.show()
