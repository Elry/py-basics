def fibRec(n, memo):
    if n <= 1:
        return n
    
    if memo[n] != -1:
        return memo[n]
    
    memo[n] = fibRec(n-1, memo) + fibRec(n-2, memo)
    return memo[n]

def fib(n):
    memo = [-1] * (n+1)
    return fibRec(n, memo)

n = 5
print(fib(n))