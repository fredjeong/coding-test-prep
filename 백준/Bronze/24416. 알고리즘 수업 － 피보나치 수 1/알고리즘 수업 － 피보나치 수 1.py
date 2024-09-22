import sys

input = sys.stdin.readline

n = int(input())

def rec_fib(N):
    global rec_count
    if N==1 or N==2:
        return 1
    else:
        return rec_fib(N-1)+rec_fib(N-2)

dp_count = n-2

print(rec_fib(n), dp_count)