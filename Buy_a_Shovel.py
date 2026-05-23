sh = list(input().split())
n =1
sh1 = sh[0]
if sh[0][-1] == sh[1]:
    n = 1    

while sh[0][-1] != sh[1]:
    if sh[0][-1] == "0":
        n = n
        break
    sh[0] = sh1 
    if sh[0][-1] != sh[1]:
        n += 1
        sh[0] = str(int(sh[0]) * n)
    

print(n)