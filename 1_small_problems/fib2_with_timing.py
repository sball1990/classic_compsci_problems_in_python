from time import time

def fib2(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib2(n-1) + fib2(n-2)

def timed_fib2(n: int) -> str:
    start = time()
    value = fib2(n)
    end = time()
    return f'The value is {value} and the time taken is {end - start}'

my_list = list(range(1, 101))
for index in my_list:
    print(timed_fib2(index))