from typing import Generator

def fib6(n: int) -> Generator[int, None, None]:
    yield 0 # special case
    if n > 0: yield 1 # special case
    last: int = 0 # initially set to fib(0)
    next: int = 1 # initially set to fib(1)

    for _index in range(1,n):
        last, next = next, last + next
        yield next  

for i in fib6(100):
    print(i)