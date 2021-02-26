def fib_efficient(n, d):
    global numFibCalls
    numFibCalls +=1
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans


def fib(n):
    global numFibCalls
    numFibCalls += 1
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


numFibCalls = 0

print(fib(35))
print('function calls:', numFibCalls)


numFibCalls = 0

d = {1:1, 2:2}
print(fib_efficient(35, d))
print('function calls:', numFibCalls)
