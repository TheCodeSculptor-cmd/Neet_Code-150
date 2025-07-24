nums = list(map(int, input("Enter number Separted by spaces: ").split()))   # Asking user to enter number for example - 2 3 4 5
target = int(input("Enter target number: "))                                # target number = 9


hashMap = {}        # Assign a empty dictionary

for i, val in enumerate(nums):
    diff = target - val
    if diff in hashMap:
        print("Indices: ", [hashMap[diff], i])
    else:
        hashMap[val] = i




# We are using enumerate to track index and val at the same time 
# In dictionary we have values like this - 2 : 0 Key : Index

