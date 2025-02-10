size=input("Enter the size of coffee : ").capitalize()
extraShot=int(input("Enter 1 for Extra shot and 0 for No Extra Shot : "))

if extraShot == 1:
    print(f'You Ordered {size} coffee with Extra Shot')
else:
    print(f'You Ordered {size} coffee with No Extra Shot')