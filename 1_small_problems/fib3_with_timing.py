from typing import Dict
from time import time

memo : Dict[int, int] = {0: 0, 1: 1} # our base cases

def fib3(n: int) -> int: 
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n-2) # memoization step
    return memo[n]

def timed_fib3(n: int) -> str:
    start = time()
    value = fib3(n)
    end = time()
    return f'The value is {value} and the time taken is {end - start}'

my_list = list(range(1, 101))
for index in my_list:
    print(timed_fib3(index))