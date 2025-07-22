s = input("Enter first string: ")
t = input("Enter second string: ")

if len(s) != len(t):
    print("false")
else:
    countS = {}
    countT = {}

    for ch in range(len(s)):
        if s[ch] in countS:
            countS[s[ch]] +=1
        else:
            countS[s[ch]] = 1

        
        if t[ch] in countT:
            countT[t[ch]] += 1
        else:
            countT[t[ch]] = 1

        

    for char in countS:
        if countS[char] != countT.get(char, 0):
            print("false")
            break
    
    else:
        print("True")
