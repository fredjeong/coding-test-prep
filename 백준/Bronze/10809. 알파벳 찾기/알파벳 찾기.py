import sys

input = sys.stdin.readline

string = input().strip()

alphabet = "abcdefghijklmnopqrstuvwxyz"

result = []
for char in alphabet:
    if char in string:
        result.append(string.index(char))
    else:
        result.append(-1)

print(" ".join(map(str, result)))