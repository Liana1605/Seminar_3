#Дан список чисел. Определите, сколько в нем встречается различных чисел.
#Input: [1, 1, 2, 0, -1, 3, 4, 4]
#Output: 6

import random

list_1 = []

for _ in range(15):
    list_1.append(random.randint(0,9))
print(list_1) 

print(set(list_1))