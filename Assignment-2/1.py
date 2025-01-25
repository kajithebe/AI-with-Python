import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

#Defining the value of x
x = np.array(range(1, 11))

#Creating y function for y1, y2, and y3
y1 = np.array(2*x + 1)
y2 = np.array(2*x + 2)
y3 = np.array(2*x + 3)

#Creating graphs (3 different subgraphs for y1, y2 and y3)
#Subgraph for y1
plt.subplot(1, 3, 1) #1 row, 3 columns
plt.plot(x, y1, color='blue', linestyle='-', linewidth=2)
plt.title("Graph of y = 2x + 1")
plt.xlabel("x")
plt.ylabel("y=2x + 1")

#Subgraph for y2
plt.subplot(1, 3, 2) #1 row, 3 columns
plt.plot(x, y2, color='black', linestyle='-', linewidth=2)
plt.title("Graph of y = 2x + 2")
plt.xlabel("x")
plt.ylabel("y=2x + 2")

#Subgraph for y3
plt.subplot(1, 3, 3) #1 row, 3 columns
plt.plot(x, y3, color='red', linestyle='-', linewidth=2)
plt.title("Graph of y = 2x + 3")
plt.xlabel("x")
plt.ylabel("y=2x + 3")

plt.tight_layout()

# Add a main title for the entire figure
plt.suptitle("Graphs of y = 2x + 1, y = 2x + 2, and y = 2x + 3")

plt.show()
