c = input()
s = input()
c1 = c.split()
c2 = list(map(int, c1))
s1= list(s)
s2 = list(map(int, s1))
x = 0
f = 0 
for i in c2:
    b = i * s2.count(x+1)
    f +=b
    x +=1
print(f)
