c = list(input())
inst = list(input())
f = 1
x = 0
for i in inst:
    if i == c[x]:
        f += 1
        x +=1


print(f)

