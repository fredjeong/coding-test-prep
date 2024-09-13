T = int(input())

from collections import deque

def solution(M, N, graph):
    visited = [False for _ in range(len(graph))]
    visited[0] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    answer = 0
    while graph:
        x, y = graph.pop()
        q.append([x, y])
        answer += 1
        while q: 
            x, y = q.popleft()
            for j in range(len(dx)):
                nx = x + dx[j]
                ny = y + dy[j]
                if [nx, ny] in graph:
                    idx = graph.index([nx, ny])
                    graph.pop(idx)
                    q.append([nx, ny])
    return answer

clear = 0
while clear < T:
    M, N, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(K)]
    if __name__ == '__main__':
        result = solution(M, N, graph)
        print(result)
    clear += 1