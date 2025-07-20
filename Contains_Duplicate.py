# Day 1 

# Contains Duplicate

nums = list(map(int, input("Enter numbers by space Separted: ").split()))

hash_set = set()                    # to store unique elements
has_duplicate = False

for n in nums:
    if n in hash_set:
        has_duplicate = True

    hash_set.add(n)

print("Contains Duplicate:", has_duplicate)