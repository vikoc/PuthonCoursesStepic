a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(a, b+1):
    for j in range(c, d+1):
        print(i*j, end=" ")
    print()
