# Input from user
word = input("Enter a String: ")

# Convert to lowercase manually (without using.lower)
lower_word = ''
for char in word:
    if 'A' <= char <= 'Z':
        lower_word += chr(ord(char) + 32)   # convert uppercase to lowercase
    else:
        lower_word += char


# Reverse manually 
reversed_word = ''

for i in range(len(lower_word) -1, -1, -1):
    reversed_word += lower_word[i]

# Check if palindrome
if lower_word == reversed_word:
    print("Palindrome!")
else:
    print("Not a palindrome!")

