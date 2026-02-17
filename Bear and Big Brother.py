limak_and_bob = input()
limak_and_bob1 = limak_and_bob.split()
lb = list(map(int, limak_and_bob1))


n = 0
while lb[1] >= lb[0]:
    lb[0] = 3*lb[0]
    lb[1] = 2*lb[1]
    n += 1
print(n)
