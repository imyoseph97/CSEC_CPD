import random
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","T","U","V","W","X","Y","Z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "'", '"', "<", ">", ",", ".", "?", "/"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
print("Welcome to the PyPassword Generator!")
l = int(input ("how many letters would you like in your password?"))
s = int(input("How many symbols would you like?"))
n = int(input("how many numbers would you like?"))
password = []
for i in range(l):
    x = random.choice(letters)
    password.append(x)
for i in range(s):
    x = random.choice(symbols)
    password.append(x)
for i in range(n):
    x = random.choice(numbers)
    password.append(x)
print(password)
random.shuffle(password)
print(password)
final = ""
for i in password:
    final += i
print(final)