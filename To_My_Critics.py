n = int(input())
for i in range(n):
    t = list(map(int, input().split()))
    if t[0] + t[1] >= 10 or t[0] + t[2] >= 10 or t[1] + t[2] >= 10:
        print("YES")
    else:
        print("NO")

