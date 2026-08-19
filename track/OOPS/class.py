class Student:
    def display(self):
        print("rollno:", self.rollno)
        print("name:", self.name)
        print("age:", self.age)
        print("marks:", self.marks)

    def study(self):
        print(self.name, "is Studied")


s1 = Student()
s1.rollno = 21
s1.name = "vinnu"
s1.age = 19
s1.marks = 98

s2 = Student()
s2.rollno = 22
s2.name = "siri"
s2.age = 28
s2.marks = 90

s1.display()
s1.study()

s2.display()
s2.study()