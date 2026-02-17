n = int(input())
f = 0
for i in range(n):
    s = input()
    s1= s.split()
    s2 = list(map(int, s1))
    if sum(s2) >= 2:
        f += 1
print(f)
