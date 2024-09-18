import sys

input = sys.stdin.readline

a, b = map(int, input().split())
a, b = min(a, b), max(a,b)

def gcd(a, b):
    idx = a
    while True:
        if a%idx==0 and b%idx==0:
            gcd = idx
            break
        idx -= 1   
    return gcd

def lcm(a, b):
    g = gcd(a, b)
    idx = b
    while True:
        if idx%a == 0 and idx%b==0:
            lcm = idx
            break
        idx += g
    return lcm

g = gcd(a,b)
l = lcm(a,b)

print(g)
print(l)