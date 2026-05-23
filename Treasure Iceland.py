print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print("Welcome to Treasure Island.\n Your mission is to find the treasure.")
print("You're at a cross road.") 
choice1 = input("Where do you want to go? \n \t Type \"left\" or \"right\"")
if choice1 == "left":
    print("You've come to a lake. There is an island in the middle of the lake")
    choice2 = input("Type \"wait\" to wait for a boat. Type \"swim\" to awim across.")
    if choice2 == "wait":
        choice21 = input("You arrive at the island unharmed. There is a house with 3 doors. one red, one yellow and one blue. Which colour do you choose?")
        if choice21 == "red":
            print("it's a room full of fire. game over.")
        elif choice21 == "yellow":
            print("you found the tressure you win!")
        elif choice21 == "blue":
            print("You enter a room of beasts. game over.")
        else:
            print("game over")
    else:
        print("you get attacked by an angry throat. game over.")
else:
    print("you fell in to the hole. game over.")