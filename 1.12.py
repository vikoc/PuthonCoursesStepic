a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c and c >= b:
    print(a)
    print(b)
    print(c)

elif b >= a and b >= c and a >= c:
    print(b)
    print(c)
    print(a)

elif c >= a and c >= b and a >= b:
    print(c)
    print(b)
    print(a)

elif c >= a and c >= b and b >= a:
    print(c)
    print(a)
    print(b)

elif a >= c and a >= b and b >= c:
    print(a)
    print(c)
    print(b)

elif b >= a and b >= c and c >= a:
    print(b)
    print(a)
    print(c)
