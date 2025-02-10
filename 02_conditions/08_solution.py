password=input("Enter your password : ")

if len(password) < 6:
    print("Your Password is Weak")
elif len(password) < 10:
    print("Your Password is Medium")
else:
    print("Your Password is Strong")