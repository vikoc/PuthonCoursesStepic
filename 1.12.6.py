n = int(input())

if n == 0 or 5 <= n <= 20 or n%10 in [0, 5, 6, 7, 8, 9] or n%100 in [0, 5, 6, 7, 8, 9] or n%100 in [11, 12, 13, 14]:
    print(n, 'программистов')


elif n == 1 or n == 21 or n%10 in [1]:
    print(n, 'программист')

elif n%10 in [2, 3, 4] or n%100 in [2, 3, 4]:
    print(n, 'программиста')
