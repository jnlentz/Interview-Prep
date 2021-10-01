def repeat(c, count):
    if count == 1:
        print(c, end='')
    else:
        print(c, end='')
        repeat(c, count-1)

def triangle(n):
    def triangleRec(i):
        if i>n: return
        repeat('#', i)
        triangleRec(i+1)
    triangleRec(1)

def wedge(n):
    def wedgeRec(i):
        if i == n:
            repeat('#', n)
        else:
            repeat('#', i)
            wedgeRec(i+1)
            repeat('#', i)
    wedgeRec(1)

def rectangle(h, w):
    if h == 1:
        if w == 1:
            print('.')
        else:
            print('.', end='')
            rectangle(1, w-1)
    else:
        rectangle(1, w)
        rectangle(h-1, w)

def pattern(n):
    if n == 1: print('X')
    else:
        pattern(n-1)
        repeat('X', n)
        pattern(n-1)

def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


