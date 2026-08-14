class studentProfile:
    def __init__(self,student_id,name,course,experience,skills):
        self.student_id=student_id
        self.name=name
        self.course=course
        self.experience=experience
        self.skills=skills 
    def __str__(self):
        return(
                f"ID:{self.student_id}\n"
                f"NAME:{self.name}\n"
                f"COURSE:{self.course}\n"
                f"EXPERIENCE:{self.experience}\n"
                f"SKILLS:{', '.join(self.skills)}"
        )

student_id=int(input("enter the student id: "))
name=input("enter the name: ")
course=input("entr the course: ")
experience=int(input("enter the experience: "))        
skills=input("enter the skills: ").split()

student=studentProfile(student_id,name,course,experience,skills)
print(student)