class Student_Profile:
    def __init__(self,stu_id,stu_name,course,score=0,skills=None,is_placed=False):
        self.stu_id=stu_id
        self.stu_name=stu_name
        self.course=course
        self.score=score
        self.skills= [] if skills is None else list(skills)
        self.is_placed=is_placed 
    def __str__(self):
        skills_text=(", ".join(self.skills) if self.skills else "Not Added")
        placement_status=("Placed" if self.is_placed else "Not Placed")
        return(f"ID:{self.stu_id}\n"
        f"NAME:{self.stu_name}\n"
        f"COURSE:{self.course}\n"
        f"SCORE:{self.score}\n"
        f"SKILLS:{self.skills}\n"
        f"PLACEMENT_STATUS:{self.is_placed}")
student=Student_Profile(102,"vinodini","python",89,["Python","Sql","Html","css"],True) 
print(student)       
    