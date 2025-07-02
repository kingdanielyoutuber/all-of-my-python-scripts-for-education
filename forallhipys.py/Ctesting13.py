#1
class Person: #teacher copying for studying
    def __init__ (self,name,age):
        self.name = name
        self.age = age
        
    def print_info(self):
        print(self.name, self.age)

man1 = Person("John",30)
man1.print_info()

#2
class Car:
    def __init__ (self,maker,model,year):
        self.maker = maker
        self.model = model
        self.year = year 
        
    def print_info(self):
        print("maker:" ,self.maker)
        print("model:" ,self.model)
        print("year:" ,self.year)
car1 = Car("Toyota","Corolla",2020)
car1.print_info()

#3
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        print(3.1415*(self.radius**2))
c = Circle(5)
c.area()
#4
class Student:
    def __init__ (self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
    
    def passed(self):
        if self.score<60:
            print(self.name, "failed")
        else:
            print(self.name, "passed")

student1 = Student("Mark",23,89)
student2 = Student("Noam",22,54)

student1.passed()
student2.passed()
#5
class Student:
    def __init__ (self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
    
    def passed(self):
        if self.score<60:
            print(self.name, "failed")
        else:
            print(self.name, "passed")

student1 = Student("Mark",23,89)
student2 = Student("Noam",22,54)

student1.passed()
student2.passed()