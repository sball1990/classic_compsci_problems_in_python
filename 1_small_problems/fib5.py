def fib5(n: int) -> int:
    if n == 0: return n # special first case
    last: int = 0 # initially set to fib(0)
    next: int = 1 # initially set to fib(1)

    for index in range(1,n):
        last, next = next, last + next
        # See Notes 1.1.5 for more details on the above assignment. It uses tuple unpacking in a concise, but perhaps less readable way.
    return next

print(fib5(5)) # 5
print(fib5(50)) # 12586269025
