
# put your python code here
a = int(input())
b = a % 400
c = a % 100
d = a % 4

if 1900 <= a <= 3000:
    if ((d == 0 and c != 0) or b== 0):
        print('Високосный')
    else:
        print('Обычный')
else:
    print('Введите число в пределах от 1900 до 3000')
