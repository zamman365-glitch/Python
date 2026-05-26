class Students:
    def __init__(self,name,age,email,number):
        self.name=name
        self.age=age
        self.email=email
        self.number=number
    def display(self):
        print(self.name)
        print(self.age)
        print(self.email) 
        print(self.number)

class Class10Admission(Students):
    def __init__(self,name,age,email,number):
        super().__init__(name,age,email,number) 
    print("admission successfull")

class Class12Admission(Students):
    def __init__(self,name,age,email,number):
        super().__init__(name,age,email,number) 
        if self.age >=16:
          print("admission successfull")
        else:
            print("admission failed")


print("press 1 for class 10th admission")
print("press 2 for class 12th admission")

choice=int(input("Enter your choice"))

name=input("tell your name:-")
age=int(input("tell the age:-"))
email=input("tell your email:-")
number=input("tell your number:-")

if choice==1:
    student1=Class10Admission(name,age,email,number)
    student1.display()


if choice==2:
    student1=Class12Admission(name,age,email,number)
    student1.display()
