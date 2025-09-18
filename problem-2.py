a = int(input("Enter a number: "))
for i in range(1, a * 2, 2):
    print(i, end=", " if i < (a * 2 - 1) else "")
