# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
calc = weight / height ** 2
bmi = round(calc)
if (int(bmi) < 18.5):
    print(f"Your BMI is {int(bmi)}, you are underweight.")
elif (int(bmi) > 18.5 and int(bmi) < 25):
    print(f"Your BMI is {int(bmi)}, you have a normal weight.")
elif (int(bmi) > 25 & int(bmi) < 30):
    print(f"Your BMI is {int(bmi)}, you are slightly overweight.")
elif (int(bmi) > 30 & int(bmi) < 35):
    print(f"Your BMI is {int(bmi)}, you are obese.")
else:
    print(f"Your BMI is {int(bmi)}, you are clinically obese.")




# Treasure game
print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction = input("Which direction do you want to go left or right? ")
if direction == "left":
    print("You chose correctly and are now at the side of a river.\n")


    river = input("Do you swim or wait for a boat? ")
    if river == "wait":
        print("You get onto a boat and make it to the other side.\n")
        doors = input("You now reach three doors which one do you go though?\nThe red door, the yellow door or the blue door?")
        if doors == "yellow":
            print("You Win!")
        elif doors == "blue":
            print("Eaten by beasts. Game Over.")
        elif doors == "red":
            print("You are burned by fire. Game Over.")
        else:
            print("Game over.")
    else:
        print("You are attacked by trout. Game Over.")

else:
    print("You Fall into a hole. Game Over.")

