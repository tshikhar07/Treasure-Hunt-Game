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
choice1 = input('you are at the crossroad.Where do you want to go?\nType"left"or"right"' ).lower()

if choice1 == "left" :
    choice2 = input('you\'ve come to a lake .There is an island in the middle of the lake.'
          'Type "wait" to wait for a boat. Type "swim"to swim across').lower()
    if choice2 == "wait":
        choice3 = input('you\'ve arrive at the island unharmed.'
              ' There is house with 3 doors. One red , One yellow , One blue.'
              ' Which color do you want to choose').lower()
        if choice3 == "red":
            print("its a room full of fire . Game Over")
        elif choice3 == "yellow":
            print("you've found the treasure .YOU WIN")
        elif choice3 == "blue":
            print("its a room full of ghosts.Game Over")
        else:
            print("Wrong choice . Game Over")
    else:
        print("you got attacked by an angry trout.Game Over.")
else:
    print("you fell in a hole.Game Over.")



