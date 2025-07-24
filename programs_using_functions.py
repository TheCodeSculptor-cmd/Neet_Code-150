
# Write a function that takes two numbers and returns their sum

def add(a, b):
    return a + b


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


result = add(num1, num2)
print("The sum is: ", result)


# Write a function that prints "Hello, [name]" where name is passed as an argument.

def greet(name):
    print("Hello", name)


user_name = input("Enter your name: ")

greet(user_name)