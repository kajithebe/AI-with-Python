import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

#Size of experiment (number of rolls)
n = [500, 1000, 2000, 5000, 10000, 15000, 20000, 50000, 100000]

for i in n:
    #Rolling two dices i times and adding the result
    dice1 = np.random.randint(1, 7, i)
    dice2 = np.random.randint(1, 7, i)
    s = dice1 + dice2

    #Computing the frequencies    
    h, h2 = np.histogram(s, bins=range(2,14))

    #Plotting the histogram
    plt.bar(h2[:-1], h/i, align='center')
    plt.title(f"Histogram of Throwing Two Dices (n = {i})")
    plt.xlabel("Sum of Two Dice")
    plt.ylabel("Probability")
    plt.xticks(range(2, 13))
    
    #Adding the result at the top of each bar
    for x, y in zip(h2[:-1], h / i):
        plt.text(x, y, f"{y*100:.1f}%", ha='center', va='bottom')
    
    plt.show()