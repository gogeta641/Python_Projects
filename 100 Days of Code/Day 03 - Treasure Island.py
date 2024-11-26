print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You have reached a crossroads. Do you want to go left or right?")
crossroads = input().lower()

if crossroads != "left":
    print("You fell into a hole. Game over!")
    exit()

print("You have now come to a river. Do you want to swim or wait?")
print("You have now come to a river. Do you want to swim or wait?")
river = input().lower()

if river != "wait":
    print("You got attached by a trout. Game over!")
    exit()

print("You have now arrived to a passage with 3 doors. One is red, the second is blue and the third is red. Which one do you go through?")
door = input().lower()

if door == "yellow":
    print("You win!")
    exit()
elif door == "red":
    print("You are burned by fire. Game over!")
    exit()
elif door == "blue":
    print("You are eaten by beasts. Game over!")
    exit()
else:
    print("Game over!")
