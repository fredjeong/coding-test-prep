N, M, V = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]

def solution_dfs(N, M, V, graph):
    arr = []
    visited = [False for _ in range(N)]
    def dfs(V, graph):
        if visited[V-1] == True:
            return
        else:
            visited[V-1] = True
            arr.append(V)
        # 자신과 연결되어 있는 노드들을 정리한다
        connected = []
        for i in graph:
            if i[0] == V:
                connected.append(i[1])
            elif i[1] == V:
                connected.append(i[0])

        # 그 중 정점의 번호가 가장 작은 간선을 선택하여 dfs 수행
        
        connected.sort()
        for j in connected:
            dfs(j, graph)
                
    dfs(V, graph)
    
    answer = ""
    for i in arr:
        answer += str(i)
        answer += " "
    answer = answer.rstrip()
    return answer

from collections import deque
import heapq

def solution_bfs(N, M, V, graph):
    
    arr = []
    visited = [False for _ in range(N)]

    def bfs(V, graph):
        q = deque()
        q.append(V)
        visited[V-1] = True

        while q:
            new_V = q.popleft()
            arr.append(new_V)
            connected = []
            for i in graph:
                if i[0] == new_V and visited[i[1]-1] == False:
                    visited[i[1]-1] = True
                    connected.append(i[1])
                elif i[1] == new_V and visited[i[0]-1] == False:
                    visited[i[0]-1] = True
                    connected.append(i[0])
                else:
                    continue
            connected.sort()
            q.extend(connected)
            connected = []
    
    bfs(V, graph)
    
    answer = ""
    for i in arr:
        answer += str(i)
        answer += " "
    answer = answer.rstrip()
    
    return answer

if __name__ == '__main__':
    result_dfs = solution_dfs(N, M, V, graph)
    result_bfs = solution_bfs(N, M, V, graph)
    print(result_dfs)
    print(result_bfs)