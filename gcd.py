a = int(input("Enter first number: "))
b = int(input("Enter Second number: "))


# Find Smaller 
if a < b:
    smaller = a 
else:
    smaller = b 


gcd = 1


for i in range(1, smaller + 1):
    if a % i == 0 and b % i == 0:
        gcd = i 
    
print("Gcd is:", gcd)