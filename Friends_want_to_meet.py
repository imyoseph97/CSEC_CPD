a = int(input())
b = int(input())

am=0
bm=0
x1 = []
x2 = []
while a!=b:
    if a > b:
        a -=1
        am +=1 
        if a>b:
            b +=1
            bm +=1
    elif a < b:
        a +=1
        am +=1
        if a<b:
            b -=1
            bm+=1
    if am not in x1:
        x1.append(am)
    if bm not in x2:
        x2.append(bm)

    

f = sum(x1) + sum(x2)
print(f)
    