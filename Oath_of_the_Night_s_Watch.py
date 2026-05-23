# Night at the Museum Solution
s = input().strip() # Use strip() to remove hidden spaces
current_pos = ord('a')
total_rotations = 0

for char in s:
    target_pos = ord(char)
    # Direct distance between letters
    diff = abs(target_pos - current_pos)
    # Choose the minimum of direct or wrap-around path
    total_rotations += min(diff, 26 - diff)
    # The pointer stays at the last letter printed
    current_pos = target_pos

print(total_rotations)