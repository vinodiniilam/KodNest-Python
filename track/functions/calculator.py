def calculate(FN,SN,OP):
    if OP=='+':
        return FN+SN
    elif OP=='-':
        return FN-SN
    elif OP=='*':
        return FN*SN
    elif OP=='/':
        return FN/SN    
FN=int(input("enter the first number: "))
SN=int(input("Enter the second number: ")) 
OP=input("enter the operator(+,-,*,/): ")
res=calculate(FN,SN,OP)
print(res)