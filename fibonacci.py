# Asking User to enter how long are fibonacci series going to be.
n = int(input("Enter the number of terms: "))

# First two terms
a, b = 0, 1

print("Fibonacci Series are:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

