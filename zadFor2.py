a = int(input())
b = int(input())
i = 0
s = 0
r = 0
if a % 3 != 0:
    a += 2
for i in range(a, b+1, 3):
    s+=i
    r+=1
       
print(s/r)
