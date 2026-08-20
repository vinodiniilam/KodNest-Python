class Student:
    def __init__(self,roll,name):
        self.__roll=roll if roll>0 else "invalid roll no"
        self.__name=name
    def setroll(self,rollno): 
        self.__roll=roll
    def getroll(self):
        return self.__roll
    def setname(self,name):
        self.__name=name    
    def getname(self):
        return self.__name 
s1=Student(-11,"vinnu")
print(s1.getroll())
print(s1.getname())           
     

