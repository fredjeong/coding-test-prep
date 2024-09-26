import sys

input = sys.stdin.readline

N = int(input())
string = input().strip()
r = 31
M = 1234567891

dic = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(alphabet)):
    dic[alphabet[i]] = i+1

total = 0
for i in range(len(string)):
    total = (total + dic[string[i]]*(r**i)) % M

print(total)