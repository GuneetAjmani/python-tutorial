n=int(input("Enter the value of n : "))
sum=0

for i in range(1,n+1):
    if i%2 == 0:
        sum+=i

print(f"Sum of Even Numbers upto {n} is : {sum}")