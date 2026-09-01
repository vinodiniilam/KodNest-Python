a=10  #its a global variable
class Employee:
    def __init__(self,id,name):      #its a constructor
        self.id=id #its a local variable
        self.name=name  # self.id is instance variable
e1=Employee(11,"Vinnu")  # e1 is an refernce object to Employee class
print(e1.id)
print(e1.name)
print(a)