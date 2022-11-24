n = 10
lst = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    lst[i][i] = n
    n -= 1
 
for line in lst:
    print(line)
    