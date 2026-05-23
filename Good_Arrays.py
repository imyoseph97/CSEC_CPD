t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 1:
        print("NO")
        continue
    
    ones = a.count(1)
    
    if sum(a) >= n + ones:
        print("YES")
    else:
        print("NO")
