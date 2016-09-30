def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''

    if char == aStr:
        return True
    elif len(aStr) > 1:
        if char >= aStr[(len(aStr) // 2)]:
            str = aStr[len(aStr) // 2:]
            return isIn(char, aStr[len(aStr) // 2:])
        elif char < aStr[(len(aStr) // 2)]:
            str = aStr[:len(aStr) // 2]
            return isIn(char, aStr[:len(aStr) // 2])
    else:
        return False

print(isIn("s","aaaas"))