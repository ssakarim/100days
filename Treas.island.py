import sys
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

direction = input(' which direction ? type "left" or "right" ? \n ').lower()

#print(type(direction))
# Checking first decision :
if direction == "left" :
  # continue in game
  secondstep=input(' You\'re at a cross road , do you choose to "swim" or "wait" ? \n').lower()
  # the backslash allow the code to escape the following character , so it is not interpreted as a closing of the first single quote; and the strat with a single quote allows us to type inside the string double quotes ..
  if secondstep== "wait" :
    # continue in game
    finalstep=input('which door you select: "blue", "red" or "yellow" ? \n').lower()
    if finalstep== "blue" :
      print("eaten by beats , game over!")
    elif finalstep=="yellow" :
      print (" You Win !!!")
    elif finalstep == "red" :
      print("Burned by fire, game over !")
    else:
      print(" Game over !")
  else:
    print (" Attached by trout, Game over")
else :
  print("Fall into a hole, game over")

print(" it was nice playing with you")


#else:
 # print("game over")
  #sys.exit(0)
