h = list(map(int, input().split()))

c = []
for i in h:
    if not i in c:
        c.append(i)
f = 4- len(c)
print(f) 