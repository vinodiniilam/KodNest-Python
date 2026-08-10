def check_sign(number):
    if number>0:
        return "positive"
    elif number<0:
        return "negative"
    else:
        return "zero"
number=int(input("Enter a number: "))
res=check_sign(number)
print(res)