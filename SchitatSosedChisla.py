a = [int(i) for i in input().split()]
m = len(a)
for i in range(0, m):
    s = 0
    if m == 1:
        print(a)
        break
    elif i == 0:
        s = a[1] + a[m-1]
        print(s, end=' ')
    elif i == m-1:
        s = a[m-2] + a[0]
        print(s, end=' ')
    else:
        s = a[i-1] + a[i+1]
        print(s, end=' ') 
    
    
