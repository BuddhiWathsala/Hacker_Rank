T = int(input())
for i in range(T):
    N = int(input())
    A = bin(N)[2:]
    B =A[1:]+A[0]
    print(int(B,2))
