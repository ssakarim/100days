height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI= round(weight /(height **2))
print(f"your BMI is {BMI} ")
if BMI <= 18.5:
  print("you are underwieght")
elif BMI <= 25:
  print("you are at normal weight")
elif BMI <= 30:
  print("you are slightly over-weight")
elif BMI <= 35:
  print(" you are Obese")
else:
  print("you arew clinically Obese")
