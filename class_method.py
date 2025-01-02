class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa+=gpa

    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    
    @classmethod
    def get_avg(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa/cls.count}"
        


stu1 = Student("shi",3.2)
stu2 = Student("adiba",3.5)
stu3 = Student("ali",2.4)
print(Student.get_count())
print(Student.get_avg())