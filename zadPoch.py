d = str(input('Ведите фигуру: прямоугольник, треугольник или круг'))

if d == 'треугольник':
    a = int(input('введите а:'))
    b = int(input('введите b:'))
    c = int(input('введите c:'))
    p = (a + b + c)/2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(s)
elif d == 'прямоугольник':
    a = int(input('введите а:'))
    b = int(input('введите b:'))
    s = a * b
    print(s)
elif d == 'круг':
    r = int(input('введите r:'))
    s = 3.14 * (r ** 2)
    print(s)
    
