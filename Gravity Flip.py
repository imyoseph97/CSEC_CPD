c = int(input())
ci = input()
ci1 = ci.split()
ci2 = list(map(int, ci1))
ci3 = []

for i in range(c):
    ci3.append(min(ci2))
    ci2.remove(min(ci2))

f = ' '.join(map(str, ci3))
print(f)
