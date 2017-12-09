def cube(n): return n**3

def fib(n):
    a, b, r = 0, 1, []
    for i in range(n):
        r.append(a)
        a, b = b, a+b
    return r

def powersOfTwo(n):
    r = []
    for i in range(n):
        r.append(2**i)
    return r