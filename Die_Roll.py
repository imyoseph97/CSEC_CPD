yw = list(map(int, input().split()))

a = 6 - (max(yw)-1)
b = 6
for i in range(1,10):
    if a % i == 0 and b % i == 0:
        a1 = int(a/i)
        b1 = int(b/i)
print(f"{a1}/{b1}")
