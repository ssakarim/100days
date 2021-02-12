# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

print(len(student_scores))

max= student_scores[0]
print("initial max is ", max)
for score in student_scores:  
    if max < score:
       max = score
       print(f"max is smaller than {score} , max = {max}")
    else:
        print(f"max is larger or equal {score}, max = {max} ")

print(f" max score is {max}")
    
    

