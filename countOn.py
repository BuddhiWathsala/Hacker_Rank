n = int(raw_input())
#n= 0
def fib(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
if n == 0:
    print 1, 0
else:
    z = fib(n-1)
    o = fib(n)
    print z, o
