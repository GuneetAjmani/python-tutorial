num=int(input("Enter the number : "))

for i in range(2,num):
    if num%i==0:
        print(f"{num} is not a prime number")
        exit()

print(f"{num} is a prime number")