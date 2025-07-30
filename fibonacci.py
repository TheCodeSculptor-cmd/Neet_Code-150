# Asking user to enter number for who long the fibonacci series should be
n = int(input("Enter a number of terms: "))

# Start With 
a, b = 0, 1

print("Fibonacci Series are:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
    