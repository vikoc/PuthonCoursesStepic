a = float(input())
b = float(input())
c = str(input())

if c == 'mod':
    if b == 0.0:
        print('Деление на 0!')
        #exit
    else:
        print(a % b)
elif c == 'pow':
    if a == 0.0 and  b < 0.0:
        print('Деление на 0!')
        #exit
    else:
        print(a ** b)
elif c == 'div':
    if b == 0.0 and c =='div':
        print('Деление на 0!')
        #exit
    else:
        print(a // b)
elif c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '/':
    if b == 0.0 and c =='/':
        print('Деление на 0!')
        #exit
    else:
        print(a / b)
elif c == '*':
    print(a * b)

    
