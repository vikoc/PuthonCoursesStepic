
a = input()
b = int(a[0])
w = int(a[1])
e = int(a[2])
c = int(a[3])
r = int(a[4])
t = int(a[5])
y = b + w + e
u = c + r + t
if y == u:
    print('Счастливый')

elif u != y:
    print('Обычный')
