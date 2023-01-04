# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
numberOfNames = len(names)
# Write your code below this line 👇
# names = "Max, George, Sarah, Greg, Mum, Dad, Gemma, Stephen"
random_number = random.randint(0, (numberOfNames-1))
# print(random_number)

# chosenName = random.choice(names) this is a much shorter way of doing it <-
chosenName = names[random_number]

print(f"{chosenName} is going to buy the meal today!")


############### x marks spot

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horz = int(position[0])
vert = int(position[1])

selected_vert = map[vert -1]
selected_vert[horz - 1] = str('X')


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")




################ Paper rock scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random


player = input("Let's play Rock, Paper, Scissors! Write your answer in... \n 3 \n 2 \n 1 \n")

ropasc = [rock, paper, scissors]

if player.lower() == "rock":
  print("\nYou chose Rock!")
  print(rock)
elif player.lower() == "paper":
  print("\nYou chose Paper!")
  print(paper)
elif player.lower() == "scissors":
  print("\nYou chose Scissors!")
  print(scissors)
else:
  print("\nYou need to select either Rock, Paper, Scissors.")

computer = random.choice(ropasc)

if computer == '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''':
  print("\nThe Computer chose Rock!")
  print(rock)
  computerChoice = "rock"
elif computer == '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''':
  print("\nThe Computer chose Paper!")
  print(paper)
  computerChoice = "paper"
elif computer == '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''':
  print("\nThe Computer chose Scissors!")
  print(scissors)
  computerChoice = "scissors"
else:
  print("Error")

if player.lower() == computerChoice:
  print("That was close thats a draw! You're both winners or losers!!")
elif player.lower() == "scissors" and computerChoice == "paper":
  print("Congratulations Scissors cut Paper! You Win")
elif player.lower() == "paper" and computerChoice == "rock":
  print("Congratulations Paper wraps Rock! You Win")
elif player.lower() == "rock" and computerChoice == "scissors":
  print("Congratulations Rock breaks Scissors! You Win")
else:
  print("Computer Wins!! You Lose!!")