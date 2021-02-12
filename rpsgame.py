import random
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
choices=[rock, paper, scissors]
#print(choices)
#print(rock)
userinput= int(input(" select 0 for rock, 1 for paper or 2 for scissors ? \n"))
if userinput >= 3 or userinput < 0: 
  print("You typed an invalid number, you lose!")
else:
 userchoice= choices[userinput]
 # above line user input is mapped to an index of the array choices to pick a user value
 # next line, computer pick a random value from the array of choices 
 computerchoice= random.choice(choices)
#print(type(computerchoice))
 print (f" \n computerchoice is {computerchoice}\n \n userchoice is {userchoice}")
 #if userinput >= 3 or userinput < 0: 
  #print("You typed an invalid number, you lose!") 
 if computerchoice ==scissors and userchoice ==paper:
  print("you lost")
 elif computerchoice == rock and userchoice == paper:
  print("you win")
 elif computerchoice==paper and userchoice == scissors:
  print("you win")
 elif computerchoice ==paper and userchoice ==rock:
  print("you lost")
 elif computerchoice ==rock and userchoice==scissors:
  print("you lost")
 elif computerchoice==scissors and userchoice==rock:
  print("you win")
 elif computerchoice == userchoice:
  print(" Draw")
 else:
  print("this is a wrong answer , youlose")

