t = int(input())
c = input()
c1 = c.split()
c2 = list(map(int, c1))
s = 0
d = 0
for i in range(t//2 + t % 2):
    x = max(c2[0], c2[-1])
    s += x
    c2.remove(x)
    if not len(c2) == 0:
        x = max(c2[0], c2[-1])
        d +=x
        c2.remove(x)
print(f"{s} {d}")
