t = int(input())
e = list(map(int, input().split()))
officers = 0
untreated = 0
for event in e:
    if event == -1:
        if officers > 0:
            officers -= 1
        else:
            untreated += 1
    else:
        officers += event
        
print(untreated)
