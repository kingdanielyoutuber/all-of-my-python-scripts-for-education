student1 = set() # create new set
student3 = set() # create new set
for i in range(3):
    student1.add(input("eneter here1:")) #add to set
    student3.add(input("eneter here2:")) #add to set
    
print("difrence between",student1.difference(student3))



print("___________--")

for t in range(20):
    if t%2 == 0:
        print(t)
    else:
        print("unequal")