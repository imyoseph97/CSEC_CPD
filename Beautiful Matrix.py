f = 0
for i in range(1,6):
    m = input()
    m1 = m.split()
    m2 = list(map(int, m1))
    if 1 in m2:
        f += abs(3 - (m2.index(1)+ 1))
        f += abs(3 - i)
print(f)
