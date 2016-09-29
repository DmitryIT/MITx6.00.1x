vowels_cnt = 0
vowels = ['a', 'e', 'i', 'o', 'u']
for char in s:
    if char in vowels:
        vowels_cnt += 1
print("Number of vowels: " + str(vowels_cnt))