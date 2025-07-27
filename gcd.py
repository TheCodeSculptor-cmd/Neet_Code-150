a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# find smaller number

if a < b:
    smaller = a 
else:
    smaller = b 

# Iterate From 1 to smaller

gcd = 1

for i in range(1, smaller + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print("GCD is:", gcd)