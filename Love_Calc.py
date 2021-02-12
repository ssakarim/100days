print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# convert input names into lower cases characters
name1l=name1.lower()
name2l=name2.lower()
#print(name1l, name2l)
# code to count the letters of the word "true " in both names
count1x=name1l.count("t")+name1l.count("r")+name1l.count("u")+name1l.count("e")
count2x=name2l.count("t")+name2l.count("r")+name2l.count("u")+name2l.count("e")
countw1= count1x+count2x
#print(countw1)

# code to count the letters of the word "love " in both names

count1y=name1l.count("l")+name1l.count("o")+name1l.count("v")+name1l.count("e")
count2y=name2l.count("l")+name2l.count("o")+name2l.count("v")+name2l.count("e")
countw2= count1y+count2y
#print(countw2)
# adding count of true to count of love into a string 
finalscoreS = str(countw1) + str(countw2)
#print(finalscoreS)

# Displaying the output to the user based on different conditions
finalscore=int(finalscoreS)
if finalscore <10 or finalscore >90  :
  print(f"Your score is {finalscore}, you go together like coke and mentos.")
elif finalscore >=40 and finalscore <=50:
  print(f"Your score is {finalscore}, you are alright together.")
else:
  print(f"Your score is {finalscore}.")
