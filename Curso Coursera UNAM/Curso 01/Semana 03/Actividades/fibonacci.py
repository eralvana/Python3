def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    return n

x=input("Number:")
y=int(x)
print(fib(y))