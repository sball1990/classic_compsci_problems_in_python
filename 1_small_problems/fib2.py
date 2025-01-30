def fib2(n: int) -> int:
    if n < 2: 
        '''
        In the Fibonacci sequence, the first two index values, 0 and 1, are NOT the sum of the previous two values and are set as the **base case** to stop the **infinitely recursive case** from fib1.py 
        '''
        return n
    return fib2(n-1) + fib2(n-2)
    '''
    The return statement above is the same as the one in fib1.py. The difference is that the base case is set to stop the recursion from going on infinitely.
    '''
