import sys
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

Bill = 0
if size=="S":
  Bill+=15
elif size=="M":
  Bill=20
elif size=="L":
  Bill=25
else:
  print("wrong size selected")
  # the sys.exit command terminates the program if the user selects something wrong and not in the 3 choices
  sys.exit(0) 
if add_pepperoni=="Y":
  if size=="S":
   Bill+=2
  else:
    Bill+=3
if extra_cheese=="Y":
  Bill+=1

print(f"your total Bill is $ {Bill}")
