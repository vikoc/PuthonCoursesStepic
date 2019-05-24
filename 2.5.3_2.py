a, b = [int(i) for i in input().split()], []
for i in a:
    if a.count(i) > 1 and b.count(i) == 0:
        b.append(i)
for i in b:
    print(i, end=" ")

