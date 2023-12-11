def solve(word):
   
    vowels = set("aeiou")
    substrings = []
    start = 0

    for i in range(len(word)):
        if word[i] in vowels:
            substrings.append(word[start:i])
            start = i + 1
    substrings.append(word[start:]) 
    substrings = [sum(ord(c) - ord('a') + 1 for c in substring) for substring in substrings]

    return max(substrings)

print(solve("strength")) 
print(solve("zodiac")) 
print(solve("phase")) 


