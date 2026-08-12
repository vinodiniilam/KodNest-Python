
class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
title=input("enter the title: ").strip() 
author=input("enter the author: ").strip() 
price=int(input("enter the price: ")) 
book=Book(title,author,price) 
print("BOOK DETAILS")
print(f"TITLE : {book.title}")
print(f"AUTHOR : {book.author}")
print(f"PRICE : {book.price}")
        
