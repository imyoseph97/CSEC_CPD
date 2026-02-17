games = int(input())
s = input()
list1 = list(s)
anton = 0
danik = 0
for i in list1:
    if i == "A":
        anton += 1
    elif i == "D":
        danik += 1
if anton > danik:
    print("Anton")
elif danik > anton:
    print("Danik")
elif danik == anton:
    print("Friendship")
