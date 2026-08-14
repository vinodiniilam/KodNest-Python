class StudentProfile:
    def __init__(self,student_id,name,course,experience,skills):
        self.student_id=student_id
        self.name=name
        self.course=course
        self.experience=experience
        self.skills=skills
student_id=input("enter the id: ")    
name=input("enter the name: ").strip()
course=input("enter the course: ").strip()
experience=int(input("enter the experience: "))
skills=input("enter the skills: ").split()
stu=StudentProfile(student_id,name,course,experience,skills)
print(f"STUDENT ID : {stu.student_id}")
print(f"NAME : {stu.name}")
print(f"COURSE : {stu.course}")
print(f"EXPERIENCE : {stu.experience}")
print(f"SKILLS : {', '.join(stu.skills)}")