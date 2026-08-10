org=[]
for i in range(3):
    org.append(int(input("enter the value: ")))
alias_score=org
replace_score=  int(input("enter the replace value: "))
additional_score=int(input("enter the additional value: "))
alias_score[0]=replace_score
alias_score.append(additional_score)  
print("original:",org)
print("Alias:",alias_score)
print("shared object",org is alias_score)