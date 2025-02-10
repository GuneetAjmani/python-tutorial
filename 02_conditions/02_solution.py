age=int(input("Enter your Age : "))
day=input("Enter today's day : ").lower()

if age >= 18 : 
    price=12
else:
    price=8

if day == 'wednesday' :
    price-=2

print("Total price is : $", price)