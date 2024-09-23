import sys

input = sys.stdin.readline

counts = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

dic = {}
for i in range(len(alphabet)):
    dic[alphabet[i]] = counts[i]

A = str(input().strip())
B = str(input().strip())

string = ""
for i in range(len(A)):
    string += str(A[i]) + str(B[i])


dp = [0 for _ in range(len(string)-1)]
dp[0] = [dic[char] for char in string]

for i in range(1, len(dp)):
    dp[i] = [int(str(dp[i-1][j]+dp[i-1][j+1])[-1]) for j in range(len(dp[i-1])-1)]

print(str(dp[-1][0]) + str(dp[-1][1]))