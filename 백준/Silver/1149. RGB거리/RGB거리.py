import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(3)] for _ in range(N)]

dp[0][0] = board[0][0]#min(board[0][1], board[0][2])
dp[0][1] = board[0][1]#min(board[0][0], board[0][2])
dp[0][2] = board[0][2]#min(board[0][0], board[0][1])

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + board[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + board[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + board[i][2]

print(min(dp[-1]))