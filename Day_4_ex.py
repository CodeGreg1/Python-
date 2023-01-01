# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
numberOfNames = len(names)
#Write your code below this line 👇
# names = "Max, George, Sarah, Greg, Mum, Dad, Gemma, Stephen"
random_number = random.randint(0, (numberOfNames-1))
# print(random_number)
chosenName = names[random_number]

print(f"{chosenName} is going to buy the meal today!")