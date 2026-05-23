t = int(input())
n = list(map(int, input().split()))
x = []
if n.count(1) >= n.count(2) and n.count(1) >= n.count(3):
    f = len(n) - n.count(1)
elif n.count(2) >= n.count(1) and n.count(2) >= n.count(3):
    f = len(n) - n.count(2)
elif n.count(3) >= n.count(1) and n.count(3) >= n.count(2):
    f = len(n) - n.count(3)
print(f)
