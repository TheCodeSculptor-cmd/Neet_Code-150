def print_multiple(limit):

    print("Multiple of 3 =", end=" ")
    for i in range(1, limit):
        if i % 3 == 0:
            print(i, end=" ")
        
    print()  # For new line


    print("Multiple of 5 =", end=" ")

    for i in range(1, limit):
        if i % 5 == 0:
            print(i, end=" ")
    
print_multiple(100)