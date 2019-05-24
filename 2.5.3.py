a = [int(i) for i in input().split()]
a.sort()
m = len(a)
s = 0
print(a, end='')
for i in range (0, m):
    for j in range (0, m):
        print(i, j, end='')
        if a[i] == a[j]:
            s += 1
            # print(a[i], end='')

