nums = list(map(int, input("Enter numbers separted by spaces: ").split()))              #  Ask User to enter for numbers in a list
target = int(input("Enter target number: "))


# Create a empty dictionary (hashmap)

hashMap = {}

# Loop through the list with index

for i, val in enumerate(nums):
    diff = target - val
    if diff in hashMap:
        print("Indices:", [hashMap[diff], i])
        break
    hashMap[val] = i



# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]