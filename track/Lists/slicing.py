word=input("enter word: ")
first=int(input("enter first index: "))
second=int(input("enter second index: "))
third=int(input("enter third index: "))
numbers=[first,second,third]
record=(first,second,third)
print(f"middle: {word[1:-1]}")
print(f"first two: {numbers[0:2]}")
print(f"reverse: {record[::-1]}")
