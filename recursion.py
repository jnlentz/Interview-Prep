def repeat(c, count):
    if count == 1:
        print(c)
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

wedge(10)