# Taking input from user 
word = input("Enter a String: ")

lower_word = ''

for char in word:
    if 'A' <= char <= 'Z':
        lower_word += chr(ord(char) + 32)
    if ('a' <= char <= 'z') or ('0' <= char <= '9'):
        lower_word += char

    
# Revered String Manually

reversed_word = ''

for i in range(len(lower_word) -1, -1, -1):
    reversed_word += lower_word[i]


# Check if Palindrom 

if lower_word == reversed_word:
    print("It's a Palindrome!")
else:
    print("It's not a palindrome")