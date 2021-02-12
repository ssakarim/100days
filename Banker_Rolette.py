# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
print(names)
# subtract 1 from the lenght of numbers to cater for the list position 0 
length= len(names)
#print(length)
#selected_name= random.
# the following line picks a random number between 0 and the number of the list members -1
selection= random.randint(0, length-1)
# printing the name in the in the position of the random selection 
print(names[selection], "is going to pay the meal today")
