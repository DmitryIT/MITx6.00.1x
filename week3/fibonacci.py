import time


num_of_calls = 0
def fibonacci(x):
    global num_of_calls
    num_of_calls+=1
    if x == 1:
        return 1
    if x == 2:
        return 2
    else:
        return fibonacci(x-1) + fibonacci(x-2)

def fibonacci_efficient(x,d):
    global num_of_calls
    num_of_calls+= 1
    if x in d:
        return d[x]
    else:
        ans = fibonacci_efficient(x-1,d) + fibonacci_efficient(x-2,d)
        d[x] = ans
        return ans

d={1:1,2:2}

start = time.time()
print(fibonacci_efficient(35,d))
end = time.time()
print(end-start)
print(num_of_calls)
