from collections import deque

N = int(input())
board = list(map(int, input().split()))
start = int(input())

def solution(N, board, start):
    visited = [False for _ in range(N)]
    visited[start-1] = True
    
    def bfs(N, board, start):
        count = 1
        q = deque()
        q.append(start-1)
        while q:
            pos = q.popleft()
            step = board[pos]
            
            arr = [pos + step, pos - step]
            for elem in arr:
                if elem < 0 or elem >= N:
                    continue
                if visited[elem] == True:
                    continue
                visited[elem] = True
                q.append(elem)
                count += 1
        return count
    return bfs(N, board, start)

if __name__ == "__main__":
    result = solution(N, board, start)
    print(result)