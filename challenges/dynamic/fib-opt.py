def fib(n):
    prevPrev, prev, curr = 0, 1, 1

    for i in range(2, n + 1):
        curr = prev + prevPrev
        prevPrev = prev
        prev = curr

    return curr

n = 5
print(fib(n))