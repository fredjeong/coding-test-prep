import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def isPrime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

if b > 10**7:
    b = 10**7

palindromes = [n for n in range(a, b+1) if str(n) == str(n)[::-1]]

for n in palindromes:
    if isPrime(n):
        print(n)
print(-1)