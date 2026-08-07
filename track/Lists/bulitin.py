n=int(input("no of values"))
lst=[]
for i in range(n):
    val=int(input("enter a number: "))
    lst.append(val)
search_score=int(input("enter the search value: ")) 
print(f"higest score: {max(lst)}")  
print(f"lowest score: {min(lst)}") 
print(f"total sum of elements: {sum(lst)}")
if search_score in lst:
    print("the search element is found")
else:
    print("not found")    
    