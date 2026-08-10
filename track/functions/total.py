def calculate_total(price,quantity):
    total=price * quantity
    return total
price=input("Enter the product price: ")
quantity=input("Enter the product quantity: ")    
res=calculate_total(int(price),int(quantity))
print("The total amount is:",res)