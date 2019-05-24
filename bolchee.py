a = int(input())
b = a % 4
c = a % 400
d = a % 100
if b == True and d == True :
    print('Обычный')
elif b == True and c == True:
    print('Высокосный')
else:
    print('Высокосный')
