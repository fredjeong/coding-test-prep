import sys

input = sys.stdin.readline

N = int(input())

if N==1:
    print("SK")
elif N==2:
    print("CY")
else:
    if N%7 in [1, 3, 4, 5, 6]:
        print("SK")
    else:
        print("CY")