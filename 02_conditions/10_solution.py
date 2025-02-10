species=input("Enter the species of pet (Dog / Cat) : ").capitalize()
age=int(input("Enter the age of your pet : "))

if species == "Dog" and age < 2:
    print("Puppy food is reccommended")
elif species == "Cat" and age > 5:
    print("Senior Cat food is reccommended")
else:
    print("Can eat Anything")