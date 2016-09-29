"""
Implementation of the bisectional search algorithm
"""

high = 1000
low  = 0
ans = (low + high) // 2
user_input = ""

print("Please think of a number between 0 and 100!")
while user_input != 'c':
    print("Is your secret number "+ str(ans) + "?")
    user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if user_input in ['h', 'l', 'c']:
        if user_input == 'h':
            high = ans
        if user_input == 'l':
            low = ans
        ans = (low + high) // 2
    else:
        print("Sorry, I did not understand your input.")
print("Game over. Your secret number was: " + str(ans))