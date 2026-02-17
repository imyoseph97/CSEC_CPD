total_and_fence = input()
vanya_friends = input()


list1 = total_and_fence.split()
list2 = vanya_friends.split()
list12 = []
for i in range(len(list2)):
    list12.append(int(list2[i]))

height = int(list1[1])
width = []

for i in list12:
    if i <= height:
        width.append(1)
    elif i > height:
        width.append(2)
min_width = sum(width)
print(min_width)
