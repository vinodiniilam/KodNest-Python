limit=int(input("enter limit:"))
total=0
number=0
while number<limit:
    if number%2==0:
        total=total+number
    number+=1
print(f"sum of even numbers is:{total}")        

