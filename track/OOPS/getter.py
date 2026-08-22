class StudentProfile:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.is_verified=False
    
    def verify(self):
        self.is_verified=True

    def get_status(self):
        print(self.is_verified)

s1=StudentProfile(12,"Vinnu")
s1.get_status()
s1.verify()
s1.get_status()
