t = int(input())
u1 = []
final = 0
for i in range(t):
    u = list(map(int, input().split()))
    u1.append(u)
print(u1)
for i in range(t):
    n=1
    if u1[i][0] == u1[i+n][1] and i+n <= t:
        final +=1
        n += 1
print(final)
