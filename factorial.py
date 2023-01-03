number = int(input("Enter a number: "))
factorial = 1
if number < 0:
    print("Negative value")
elif number == 0:
    print("Factorial is 1")
else:
    for i in range(1, number + 1):
        factorial = factorial * i
    print(f"Factorial of {number} is {factorial}")
