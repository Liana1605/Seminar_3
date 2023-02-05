#Дана последовательность из N целых чисел и числа K. Необходимо сдвинуть всю последовательность
#(сдвиг - циклический) на K элементов вправо, K – положительное число.
#Input: [1, 2, 3, 4, 5] k = 3
#Output: [4, 5, 1, 2, 3]

import random

list_1 = []

k = int(input('Введите число k: '))

for _ in range(9):
    list_1.append(random.randint(0, 5))
print(list_1) 

list_1 = list_1[k:] + list_1[:k] 

print(list_1)