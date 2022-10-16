import random

A = [0, 1/4]
B = [1/4, 2]
C = [1/2, 3/4]
D = [3/4, 1]

n = 20

count_a, count_b, count_c, count_d = 0, 0, 0, 0


def calculate(value):
    return round(4*value*(1-value), 2)


for _ in range(n):
    num = round(random.random(), 2)
    result = calculate(num)

    if result in A:
        count_a += 1
    elif result in B:
        count_b += 1
    elif result in C:
        count_c += 1
    elif result in D:
        count_d += 1

print("A set total: ", count_a)
print("B set total: ", count_b)
print("C set total: ", count_c)
print("D set total: ", count_d)