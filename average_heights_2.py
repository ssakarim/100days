# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights \n ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
print(f"The list fo students heights is {student_heights} ")
#print(len(student_heights))
total = 0
for i in student_heights:
  total+= i
print(total)

number_of_students = 0
for x in student_heights:
  number_of_students+= 1
print(number_of_students)

#for i in range(0, len(student_heights)):
  #total+= student_heights[i]
#print(total)
average = round(total / number_of_students)
#average_whole = round(average)
print (f"The average students heights is {average} cm's ")
