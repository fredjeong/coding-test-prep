import sys
sys.setrecursionlimit(10**8)
#dfs
def dfs(x,y):
    if x<= -1 or x >= n or y <= -1 or y >= m:
        return False
    if board[x][y] == 1:
        board[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False
    
t = int(input())
for i in range(t):
    m,n,k = map(int, sys.stdin.readline().split())
    board = [[0]*(m) for h in range(n)]
    for j in range(k):
        u_y,v_x = map(int, sys.stdin.readline().split())
        board[v_x][u_y] = 1 
    cnt = 0
    for a in range(n):
        for b in range(m):
            if dfs(a,b) == True:
                cnt += 1
    print(cnt)