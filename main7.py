import random
res = [random.randrange(-2000, 5000) for i in range(10)]
print ("рандомный списочек чисел: " +  str(res))
a = max(res)
print("максимальное число: ", a)
b = min(res)
print("минимальное число: ", b)
i = 0
print('cумма положительных чисел:', sum(i > 0 for i in res))
print('сумма отрицательных чисел:', sum(i < 0 for i in res))
