userInput = int(input("Enter a Number: "))
print("The factors of", userInput, "is/are: ")
for x in range(1, userInput + 1):
    if userInput % x == 0:
        print(x)
