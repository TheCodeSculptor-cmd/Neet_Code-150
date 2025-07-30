def print_multiples(limit):

    print("Multiples of 3 =", end=" ")
    for i in range(1, limit):
        if i % 3 ==  0:
            print(i, end=" ")

    print() # For new line


    print("Multiples of 5 =", end=" ")
    for i in range(1, limit):
        if i % 5 == 0:
            print(i, end=" ")

        
print_multiples(20)
