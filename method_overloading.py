
# method overloading
class Demo:
    def add(self,*args):
        total = 0
        for i in args:
            total = total + i

        return total
d =  Demo()
print(d.add(2,3,4,5))
# ----------------------------------------------
method overriding
class Father:
    def sleep(self):
        print("sleep tight")
    def eat(self):
        print("just eating")

class daughter(Father):
    def sleep(self):
        print("sleeping is fun")
        super().sleep()

shirin = daughter()
shirin.sleep()
# ---------------------------------------
# method overriding
class Person:
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print("vaat meat")
    def exercise(self):
        raise NotImplementedError


class Cricketer(Person):
    def __init__(self, name, age, height, weight,team):
        self.team = team
        super().__init__(name, age, height, weight)

    def eat(self):
        print("vegetables")
    
    def exercise(self):
        print("we also exercise")

sakib = Cricketer("sakib",38,66,91,"BD")
rakib = Cricketer("rakib",20,55,66,"BD")
sakib.eat()
sakib.exercise()


# --------------------------------
# method overloading
class Person:
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print("vaat meat")
    def exercise(self):
        raise NotImplementedError


class Cricketer(Person):
    def __init__(self, name, age, height, weight,team):
        self.team = team
        super().__init__(name, age, height, weight)

    def eat(self):
        print("vegetables")
    
    def exercise(self):
        print("we also exercise")
    def __add__(self,other):
        return self.age + other.age

sakib = Cricketer("sakib",38,66,91,"BD")
rakib = Cricketer("rakib",20,55,66,"BD")
print(sakib+rakib)

