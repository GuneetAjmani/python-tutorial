numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

cnt=0
for num in numbers:
    if num > 0:
        cnt+=1

print(f"List Number have {cnt} positive numbers")