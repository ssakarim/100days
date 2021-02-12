# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

print(len(student_scores))

max= student_scores[0]
for n in range (0, len(student_scores)-1):    
    if max >= student_scores[n+1]:
       max = max
     #student_scores[n] = max
    else:
       max= student_scores[n+1]
     #student_scores[n+1]=max

print(f" max score is {max}")
    
    

