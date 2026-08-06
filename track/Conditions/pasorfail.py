n=int(input("enter no of students: "))
passed_count=0
failed_count=0
total_marks=0
for i in range(n):
    name=input("enter the name: ")
    marks=int(input("enter the marks: "))
    total_marks=total_marks+marks
    if marks>=35:
        passed_count+=1
    else:
        failed_count+=1
print(f"passed count: {passed_count}")
print(f"failed count: {failed_count}")
print(f"total marks: {total_marks}")
if passed_count==0:
    print("Excellent batch")
else:
    print("batch needs improvement")    
