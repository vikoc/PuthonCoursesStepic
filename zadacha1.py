a = int(input())
b = int(input())
c = int(input())
p = ( a + b + c ) / 2
s1 = p - a
s2 = p - b
s3 = p - c
s4 = (s1 * s2 * s3) * p
s = s4 ** 0.5
print(s) 
