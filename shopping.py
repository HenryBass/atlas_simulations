import random

p1 = 0.3
p2 = 0.4
cmin = (1/7)

mincount = 0
maxcount = 0
its = 10_000_000

"""
Reasoning: 

(b - c) is the probability of Sunday given not shopping on Saturday

Min:

0.3(b + c) + 0.7(b - c) = 0.4 (Restricts average to 0.4)

b + c = 1 (Upper bound)

b - c = 0.1/0.7

Min = 1/7

Max:

0.3(b + c) + 0.7(b - c) = 0.4 (Restricts average to 0.4)

b + c = 0 (Lower bound)

0.7(b - c) = 0.4

b - c = 0.4/0.7

Max = 4/7
"""

for i in range(its):
    if random.random() < p1:
        mincount += 1
        maxcount += 1
    else:
        if random.random() < (1/7):
            mincount += 1
        if random.random() < (4/7):
            maxcount += 1

print("Min:")
print((mincount/its) * 100)
print("Max:")
print((maxcount/its) * 100)