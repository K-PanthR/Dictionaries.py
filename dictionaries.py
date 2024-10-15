Student={"Name":"Hashim" , "Age":12 , "Height":169.3 , "Weight":96 , "Eye Colour":"Brown"}
print(Student)
print(Student["Age"])
for i in Student:
    print(i)
for i in Student:
    print(Student[i])
Student["Coding"]=True
print(Student)
del Student["Weight"]
print(Student)
print(Student.keys())
print(Student.values())
print(len(Student))
