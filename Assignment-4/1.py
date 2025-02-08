import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

n = [500, 1000, 2000, 5000, 10000, 15000, 20000, 50000, 100000]

for i in n:
    dice1 = np.random.randint(1, 7, i)
    dice2 = np.random.randint(1, 7, i)
    s = dice1 + dice2

    # print(s)
    h, h2 = np.histogram(s, bins=range(2,14))

    print(f"h: {h}")
    print(f"h2: {h2}")

    plt.bar(h2[:-1], h/i, align='center')
    plt.title(f"Histogram of Throwing Two Dices (n = {i})")
    plt.xlabel("Sum of Two Dice")
    plt.ylabel("Probability")
    plt.xticks(range(2, 13))
    
    for x, y in zip(h2[:-1], h / i):
        plt.text(x, y, f"{y*100:.1f}%", ha='center', va='bottom')
    
    plt.show()