limit=int(input("enter the limit: "))
t=int(input("enter thr traget value: "))
found=False
count=0
total=0
for i in range(1,limit+1):
    if i%3==0:
        count+=1
        total+=i
        if i==t:
             found=True
print(f"Count:{count}")            
print(f"Total:{total}") 
if found:
    print("target found")
else:
    print("target not found")    