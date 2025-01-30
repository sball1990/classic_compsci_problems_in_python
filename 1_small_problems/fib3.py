from typing import Dict

memo : Dict[int, int] = {0: 0, 1: 1} # our base cases

'''

Don't be overwhelmed by the type annotation. It's just a way to tell Python that memo is a dictionary that maps integers to integers.

This is functionally equivalent to: 

memo = {0: 0, 1: 1}

'''
def fib3(n: int) -> int: 
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n-2) # memoization step
    return memo[n]

'''
What this does, instead of calculating each time, stores the result of the calculation in a dictionary called memo. It then checks if the result is already in the dictionary. If it is, it returns the result. If it isn't, it calculates the result, stores it in the dictionary, and then returns it.

This is NOT just for each function call, but even the inside recursive calls. E.g. for fib3(100), it doesn't just check memo for fib3(100), but also as required for the recursive calles fib3(99), which is [n-1], and fib3(98), which is [n-2], and so on.
'''

