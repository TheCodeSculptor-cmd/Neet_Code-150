a = int(input("Enter first nummber: "))
b = int(input("Enter Second number: "))

# Find Smallst

if a < b:
    smallest = a
else:
    smallest = b


gcd = 1


for i in range(1, smallest):
    if a % i == 0 or b % i == 0:
        gcd = i

print(f"GCD for {a} and {b} =",gcd)