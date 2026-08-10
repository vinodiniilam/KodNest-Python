skills=[]
for i in range(5):
    val=input("enter the skills: ")
    skills.append(val)
skill_record=tuple(skills)
print(f" the tuple is: {skill_record}")
print(f"the first three is: {skill_record[0:3]}")
print(f"the last two is: {skill_record[3:]}")
print(f"alternative skils are: {skill_record[0:5:2]}")
print(f"the reverse of tuple is: {skill_record[::-1]}")


