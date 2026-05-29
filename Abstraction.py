"""from abc import ABC , abstractmethod

class shapes(ABC):
    @abstractmethod
    def area():
        pass 


    @abstractmethod
    def perimeter():
        pass

class square(shapes):
    def __init__(self,side):    
        self.side = side 




    def perimeter(self): 
        print(4*self.side)



    def area(self):
        print(self.side*self.side)




class circle(shapes):
    def __init__(self,radius):
        self.radius = radius


    def area():
        pass

    def perimeter():
        pass        



obj = square(10)"""    


"""class robots:
    a= 12
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"the name of the robot is {self.name}"

obj = robots("alpha1")
obj2 = robots("beta1")
print(obj)
print(obj2)"""  



"""class numbers:
    def __init__(self,value):
        self.value = value


    def __add__(self,other):
        return self.value + other.value
    

    def __eq__(self,value):
        return self.value == value.value
a = numbers(20)        
b = numbers(30)
print(a + b)
print(a == b)"""