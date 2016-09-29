"""
Test DocString
"""
def f(x):
    x = x[::-1]
    print(id(x))
    return x


x = "abcdefg"
print(id(x))
x = f("%s" % x)
print(id(x))
