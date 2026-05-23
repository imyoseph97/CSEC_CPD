t = int(input())
f = []
n = 0
f1 = []
for i in range(t):
    m = list(input().split())
    f.append(m)



for i in range(t):
    if f[i][1] == "rat":
        f1.append(f[i][0])
for i in range(t):
    if f[i][1] == "woman" or f[i][1] == "child":
        f1.append(f[i][0])
for i in range(t):
    if f[i][1] == "man":
        f1.append(f[i][0])
for i in range(t):
    if f[i][1] == "captain":
        f1.append(f[i][0])    




for i in f1:
    print(i)