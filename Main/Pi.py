import math as mt
import random as rd

MAX = 100000

count = 0

for i in range(MAX):
    dist = mt.sqrt((rd.random() ** 2) + (rd.random() ** 2))
    if dist <= 1:
        count += 1
print(4*(count/MAX))
