# class factory:
#     a = 12 #this is an attribute

#     def listen(): #this is a method 
#         print("hello how are you")


# print(factory.a) #accessing attributes 
# factory.listen() #accessing methods  





# ###OBJECTS

# class hello:
#     a = 12
#     def speak(self):
#         print(self)
#         print("how are you")

# obj = hello() #created an OBJECT


# print (obj.a) #object can also access attribute

# obj.speak() #when we use objects to call any method 
#             #inside class we always sens location of my priject



# class factory:
#     def __init__(self): # constructor function is called whenever a new object is created 
#         print("how are you") # and this self will target the location of any objects 

#     print("yhis is p23 batch")

# a = factory()
# b = factory()
# c = factory()

# #2nd use of constructor 


# class factory:
#     def __init__(self,zips,pockets,material):
#         self.zips = zips
#         self.pocets = pockets
#         self.material = material

#     def details(self):
#         print("your bag details are :-")
#         print(self.zips)
#         print(self.pockets)
#         print(self.material)

# reebok = factory(2,2,"leather")

# campus = factory(4,2,"plastic")


# class Registration:
#     age = 18 #calss attribute 

#     def __init__(self,name,email,age,number):
#         if age>= Registration.age:
#             self.name = name #object attribute
#             self.email = email
#             self.number = number
#         else:
#             print("you cannot register you are underage")
#             return
        
#     def detais(self):  #object method - it target the location of object of self will take the location of the object whichever object is calling
#         print(self.name)
#         print(self.email)
#         print(self.number)
#         print(self.number)
#         print(self.age)

#     @classmethod
#     def dummy_details(cls):#class method - it is always  access the location of your class
#         print(cls.name)
#         print(cls.email)
#         print(cls.number)
#         print(cls.number)
#         print(cls.age)

#     @staticmethod #static method :- it does not take any location of class and object
#     def college_details(): #this method will not target any location
# obj=Registration("Nikhil","nikhil1234@gmail.com",23,7804070999)
# obj.detais()



#Inheritance 

#one class attributes and methods can be accessed by another class this thing is known as inheritance 

# class bhopalfactory:
#     Reg_num = 15484122841
#     def __init__(self,color,size,type):
#         self.color = color
#         self.size = size
#         self.type = type


#     def details(self):
#         print("your shoes details are :")
#         print(self.color)
#         print(self.size)
#         print(self.size)

# class indorefactory(bhopalfactory):
#     def __init__(self,color,size,type,price):
#         super().__init__(color,size,type)
#         self.price = price

# class ujjainfactory(indorefactory):
#     def __init__(self, color, size, type, price):
#         super().__init__(color, size, type, price)



# shoe1 = bhopalfactory("Red",8,"jordan")
# shoe2 = indorefactory("yellow",7,"sneakers",7999)
# shoe2.details()



# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def details(self):
#         print(self.name)

# class Human:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         print("hello human you speak")

# class Robot(Animal,Human):
#     def __init__(self, name ,age):
#         Human.__init__(self ,name,age)
    

# obj = Robot("Alpha",2)


#Hierarchical inheritance
# class Animal:
#     pass
# class Human(Animal):
#     pass
# class Robot(Animal):
#     pass    

#hybrid inheritance

# class Animal:
#     pass
# class Human:
#     pass
# class Robots(Animal,Human):
#     pass
# class AI(Robots):
#     pass





# class Animal:
#     name = "lion"

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# class Human:
#     name = "Nikhil"

#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def details(self):
#         print("the details are:")
#         print(self.name)
#         print(self.age)
#         print(self.gender)

# obj1 = Animal("giraffe",6)
# obj2 = Human("Nikhil",21,"male")




# class bhopalfactory:
#     Reg_num = 15484122841
#     def __init__(self,color,size,type):
#         self.color = color
#         self.size = size
#         self.type = type


#     def details(self):
#         print("your shoes details are :")
#         print(self.color)
#         print(self.size)
#         print(self.size)

# class indorefactory(bhopalfactory):
#     def __init__(self,color,size,type,price):
#         super().__init__(color,size,type)
#         self.price = price
#     def details(self):
#         print(super().details())
#         print(self.price)



# shoe2 = indorefactory("yellow",7,"sneakers",7999)
# shoe2.details()
#this obj can now only call one method that is of indorefactory it of indore factory it cannot be call bhopalfactory details method and this thing is known as meethod overriding 

# method overloading 
# class Animal:
#     def hello():
#         pass
#     def hello(a,b):
#         pass

# obj=Animal()
# obj.hello(12,45)
# dono cheezen dene padenge akela ek nhi de payenge
# same name methods inside a single class but with different parameters this thing is knowns as method overloading it is not available in python



                                         #enscapsulation 
#protecting the attributes and methods is known as enscapsulation
# We use access modifier 
class Animal:
    a = 12 #public attribute 
    b = 23 #protected attribute
    c = 45 #private attribute 

    def hello(self): #public method
        print("how are you")
    def _hello2(self): #protected method
        print("hoe are you2")
    def __hello3(self):
        print("how are you3")    

obj = Animal()
print(obj.a)



                               # Abstraction

# @abc use karna padhta hai 
# showing only essential features and hide the background details is knowns as Abstraction.

from abc import ABC, abstractmethod
class person(ABC):
    @abstractmethod 
    def info():
        pass
    @abstractmethod 
    def register():
        pass

class Teacher(person):
    def info():
        pass
    def register():
        pass
class Students(person):
    def info():
        pass
    def register():
        pass

obj=Teacher()