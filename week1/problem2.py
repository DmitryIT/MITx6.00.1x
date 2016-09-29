s = "jvaeqkmdacgr"
search_str = "bob"
str_cnt = 0
while s.find(search_str) != -1:
    str_cnt += 1
    s = s[s.find(search_str) + 1:]
print("Number of times "+search_str+" occurs is: " + str(str_cnt))




