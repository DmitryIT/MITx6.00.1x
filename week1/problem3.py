s = "abcbcd"
previous_char = ""
longest_str = ""
current_str = ""
for char in s:
    if char >= previous_char: #still in word
        previous_char = char
        current_str += char
    else:
        if len(current_str) > len(longest_str):
            longest_str = current_str
            current_str = ""
            previous_char = char
            current_str += char
        else:
            current_str = ""
            previous_char = char
            current_str += char

if len(current_str) > len(longest_str):
    longest_str = current_str
print(longest_str)


s = "azcbobobegghakl"
previous_char = ""
longest_str = ""
current_str = ""

for char in s:
    if previous_char > char and len(current_str) > len(longest_str):
        longest_str = current_str
        current_str = ""
    elif previous_char > char and len(current_str) <= len(longest_str):
        current_str = ""

    previous_char = char
    current_str += char

if len(current_str) > len(longest_str):
    longest_str = current_str
print("Longest substring in alphabetical order is: " + longest_str)
