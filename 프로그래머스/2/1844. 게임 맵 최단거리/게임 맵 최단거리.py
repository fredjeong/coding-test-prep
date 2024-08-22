# 최단거리를 찾는 bfs 문제이므로 deque를 사용한다
from collections import deque

def solution(maps):
    rows = len(maps)
    cols = len(maps[0])
    visited = [[False for _ in range (cols)] for _ in range(rows)]
    visited[0][0] = True
    
    q = deque()
    q.append((0, 0))
    
    # 동서남북 이동방향 정의
    drow = [1, -1, 0, 0]
    dcol = [0, 0, 1, -1]
    while q:
        row, col = q.popleft() # 맨 앞에 있는 (0,0)을 가져온다
        for i in range(len(drow)):
            new_row = row + drow[i]
            new_col = col + dcol[i]
            
            if 0 <= new_row < len(maps) and 0 <= new_col < len(maps[0]) and maps[new_row][new_col] == 1:
                if not visited[new_row][new_col]:
                    visited[new_row][new_col] = True
                    q.append((new_row, new_col))
                    maps[new_row][new_col] = maps[row][col] + 1
    
    if maps[len(maps)-1][len(maps[0])-1] == 1:
        answer = -1
    
    else:
        answer = maps[-1][-1]
    
    return answer