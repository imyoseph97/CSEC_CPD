t = int(input())
c = input().upper()
c1 = c.split()
c2 = 0
for i in range(t):
    if not i == t-1 and c[i] == c[i+1]:
        c2+=1
print(c2)
