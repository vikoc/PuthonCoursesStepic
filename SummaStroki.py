a = [int(i) for i in input().split()]
i = 0
m = len(a)-1
s = 0
for i in range (0, m+1):
    s = s + a[i]

print(s)
