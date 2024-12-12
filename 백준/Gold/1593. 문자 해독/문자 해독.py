import sys
input = sys.stdin.readline

length_w, length_s = map(int, input().split())
w = input().strip()
s = input().strip()
sorted_w = sorted(w)

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

dic_w = {}
dic_s = {}

for char in chars:
    dic_w[char] = 0
    dic_s[char] = 0

count = 0

for char in w:
    dic_w[char] += 1

for i in range(length_w):
    dic_s[s[i]] += 1

if dic_s == dic_w:
    count += 1

for i in range(1, length_s - length_w + 1):
    dic_s[s[i-1]] -= 1
    dic_s[s[i+length_w-1]] += 1

    if dic_s == dic_w:
        count += 1

print(count)