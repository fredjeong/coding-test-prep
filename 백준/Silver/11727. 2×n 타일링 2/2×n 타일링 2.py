import sys

input = sys.stdin.readline

N = int(input())

def calc(a, b):
    # a+bCa
    numer = 1
    denom = 1
    for i in range(1, a+1):
        numer *= a+b+1-i
        denom *= i
        
    return (numer//denom)*(2**b)

if N%2==0:
    total = 0
    for a in range(0, N+1, 2):
        b = (N-a)//2
        total = (total + calc(a, b))%10007
elif N%2==1:
    total = 0
    for a in range(1, N+1, 2):
        b = (N-a)//2
        total = (total + calc(a, b))%10007
print(total)