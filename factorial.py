num = int(input("Enter a number for which you want a Factorial: "))

factorial = 1                   # To track the value and multiplying with 1 does'nt effect the result

for i in range(1, num + 1):
    factorial = factorial * i

print(f"Factorial of {num} = {factorial}")   