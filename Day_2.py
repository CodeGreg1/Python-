# If the bill was $150.00, split between 5 people, with 12% tip.

bill = input("What is the amount of the bill?\n£")
people = input("How many do you need to split the bill to?\n")
tip = input("What percentage tip would you like to give?\n10%, 12% or 15% \n")

amount = float(bill) * ((int(tip)/100)+1) / int(people)

rounded = format(amount, '.2f')

print(f"You should pay each £{rounded}")

#  Each person should pay (150.00 / 5) * 1.12 = 33.6
#  Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling
# to solve this.💪

# Write your code below this line 👇
