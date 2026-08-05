marks=int(input("enter the marks:"))
atten=float(input("enter the attendence:"))
proj_status=input("enter project_status")
if marks>=60 and atten>=75:
    if proj_status=="yes":
        print("eligible")
    else:
        print("complete the project")
else:
    print("not eligible")       
