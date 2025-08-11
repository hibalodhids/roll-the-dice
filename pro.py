import numpy as np

n = int(input("How many Dice do you wanted to roll?"))
rolls = np.random.randint(1, 7, size=n)

print("Your rolls:", rolls)

print("Total:",np.sum(rolls))
print("Average:", np.mean(rolls))
print("Frequency:", np.bincount(rolls)[1:])