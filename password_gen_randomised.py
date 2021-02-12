#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P




#print(letters_selected)
password = []
for l in range (0, nr_letters):
  letters_selected = random.choice(letters)
  password.append(letters_selected)
#print(password)

for n in range (0, nr_numbers):
  numbers_selected = random.choice(numbers)
  password.append(numbers_selected)
#print(password)

for s in range (0, nr_symbols):
  symbols_selected = random.choice(symbols)
  password.append(symbols_selected)
print(password)
random.shuffle(password)
print(password)

for p in password:
  print(*p, end='')
print("\n")

#password_gen=""
#for p in password:
#  password_gen+= p
#print(password_gen)