year=int(input("Enter the year : "))

if (year % 400 == 0) or (year % 4 == 0 and year %100 != 0) :
    print("Year is Leap Year")
else:
    print("Year is Non-Leap Year")