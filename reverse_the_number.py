num = int(input("Enter the numbers: "))              # For example - 789
original_num = num                                   # I am saving my user input to use it in a print statement    
reverse = 0

while num != 0:
    digit = num % 10                            # With the help of % I can take the last digit out
    reverse = reverse * 10 + digit              # The element which we take out now I am moving that element to the left side and adding the current element
    num = num // 10                             # This will remove the element which has been used

print(f"The reverse of {original_num} = {reverse}")