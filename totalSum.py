totalSum = 0
counter = 1
n = int(input("Enter number: "))

while counter <= n:
    totalSum += counter
    counter += 1

print(f"The sum of numbers from 1 to {n} is ", totalSum)
