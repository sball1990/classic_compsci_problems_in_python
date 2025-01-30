from time import time

def fib5(n: int) -> int:
    if n == 0: return n # special first case
    last: int = 0 # initially set to fib(0)
    next: int = 1 # initially set to fib(1)

    for index in range(1,n):
        last, next = next, last + next
        # See Notes 1.1.5 for more details on the above assignment. It uses tuple unpacking in a concise, but perhaps less readable way.
    return next

def timed_fib5(n: int) -> str:
    start = time()
    value = fib5(n)
    end = time()
    return f'The value is {value} and the time taken is {end - start}'

my_list = list(range(1, 101))
for index in my_list:
    print(timed_fib5(index))