m = int(input())

p1 = input()
c= 1
for i in range(m-1):
    p = input()
    if p1 != p:
        c += 1
    p1 = p
       
print(c)
