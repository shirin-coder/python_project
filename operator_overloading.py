class ComplexNum:
    def __init__(self,r,i):
        self.real = r
        self.imaginary = i

    def __add__(self,other):
        return f"{self.real + other.real} + {self.imaginary + other.imaginary}i"
    
c1 = ComplexNum(1,2)
c2 =  ComplexNum(4,5)
print(c1+c2)


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __gt__(self,other):
        if self.age > other.age:
            return True
        else:
            return False

p1 = Person("shirin",19)
p2 = Person("adiba",2)
if p1>p2:
    print(f"{p1.name} will pay the bill")

else:
    print(f"{p2.name} will pay the bill ")
