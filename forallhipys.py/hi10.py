course = {"History","Math","Computers","English"}
course.add("Shelch")
print(course)



print("  _________   ")



set1 = {"History","Math","Computers","English"}
set2 = {"Math","Computers", "Art", "Design"}

print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))


print(" ____________________________             ")


student1 = set() #create a new set
student2 = set() #create a new set

'''
lets user input 4 times
every input is added to the set accordingly
'''
print("student 1:")
for i in range(4):
    student1.add(input("Enter a course:"))
    
print("student 2")
for i in range(4):
    student2.add(input("Enter a course:"))

print("same classes:",student1.intersection(student2)) 
print("student 1 but not student 2:" ,student1.difference(student2))

print("_______________________")