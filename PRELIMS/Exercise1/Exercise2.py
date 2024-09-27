userInput = int(input("Enter a number: "))
num = 0
factorial = 1
for x in range(1, userInput + 1):
    factorial = factorial * x
print("The factorial of", userInput, "is", factorial)
