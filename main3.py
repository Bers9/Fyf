#ЗАДАНИЕ 3
a = int(input("Введите ширину: "))
b = int(input("Введите высоту: "))
 
for i in range(b):
    if i == 0 or i == b - 1:
        for j in range(a):
            print('*', end=' ')
    else:
        print('*', end=' ')
        for j in range(1, a - 1):
            print(' ', end=' ')
        print('*', end=' ')
    print()