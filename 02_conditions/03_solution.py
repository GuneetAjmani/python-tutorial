marks=int(input("Enter your marks : "))

if marks > 100 or marks < 0:
    print("Invalid Marks ")
    exit()

if marks >=90:
    grade='A'
elif marks >=80:
    grade='B'
elif marks >=70:
    grade='C'
elif marks >=60:
    grade='D'
else:
    grade='F'

print("Your Grade is ", grade)