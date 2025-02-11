s=input("Enter the string : ")

for char in s:
    if s.count(char) ==1:
        print("The first non repeating character is : ", char)
        exit()

print("There is no non repeating character ")