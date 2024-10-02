import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

cumsum = [[0 for _ in range(n)] for _ in range(n)]
cumsum[0][0] = board[0][0]
for i in range(n):
    cumsum[i][0] = board[i][0] + cumsum[i-1][0]

for j in range(n):
    cumsum[0][j] = board[0][j] + cumsum[0][j-1]

for i in range(1, n):
    for j in range(1, n):
        cumsum[i][j] = board[i][j] + cumsum[i-1][j] + cumsum[i][j-1] - cumsum[i-1][j-1]

for _ in range(m):
    start_x, start_y, end_x, end_y = map(int, input().split())
    start_x -= 1
    start_y -= 1
    end_x -= 1
    end_y -= 1
    if start_x==0 and start_y==0:
        val = cumsum[end_x][end_y]
    elif start_x==0 and start_y!=0:
        val = cumsum[end_x][end_y] - cumsum[end_x][start_y-1]
    elif start_x!=0 and start_y==0:
        val = cumsum[end_x][end_y] - cumsum[start_x-1][end_y]
    else:
        val = cumsum[end_x][end_y] - cumsum[start_x-1][end_y] - cumsum[end_x][start_y-1] + cumsum[start_x-1][start_y-1]
    print(val)