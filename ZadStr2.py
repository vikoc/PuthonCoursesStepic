gen = input()
gen1 = gen.upper()
c = gen1.count('C')
g = gen1.count('G')
i = len(gen)
s = ((c + g)/i)*100
print(s)
