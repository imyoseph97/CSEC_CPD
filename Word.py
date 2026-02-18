w= input()
cu = 0
cl = 0 
for i in range(len(w)):
    if w[i].isupper():
        cu += 1
    else:
        cl +=1
if cu > cl:
    w1 = w.upper()
elif cu < cl or cu == cl:
    w1 = w.lower()
print(w1)
