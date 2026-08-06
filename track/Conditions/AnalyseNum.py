n=int(input("enter the  range:"))
PC=0
NC=0
ZC=0
T=0
for i in range(n):
    num=int(input("enter the number:"))
    T=T+num
    if num>0:
        PC+=1
    elif num<0:
        NC+=1
    else:
        ZC+=1
print(f"the positive count is: {PC}")
print(f"negative count is: {NC}")
print(f"zero count is:{ZC}")
print(f"total as: {T}")