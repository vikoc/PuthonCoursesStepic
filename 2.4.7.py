a = input()
s = 1

for i in range (0, len(a)):

    if len(a) == 1:
            print(a[i], s, sep = '', end = '')
            break
    
    if a[i] == a[i + 1]:
        s += 1
        if i == (len(a) - 2):
            print(a[i], s, sep = '', end = '')
            break
        
    elif a[i] != a[i + 1]:
 
        print(a[i], s, sep = '', end = '')
        s = 1
        if i == (len(a) - 2):
            print(a[i+1], 1, sep = '', end = '')
            break 
        continue
        

