import sys
N = int(input())
connected = int(input())
graph = [list(map(int, input().split())) for _ in range(connected)]

from collections import deque

def solution(N, connected, graph):
    visited = [False for _ in range(N)]
    global answer
    answer = 0

    def bfs(node):
        global answer
        q = deque()
        q.append(node) # 찾고자 하는 노드를 넣는다
        visited[node-1] = True
        while q:
            # q가 비어있지 않다면
            cur_node = q.popleft()
            for i in range(1, N+1):
                if [cur_node, i] not in graph and [i, cur_node] not in graph:
                    continue
                else:
                    if [cur_node, i] in graph:
                        new_node = i
                    elif [i, cur_node] in graph:
                        new_node = i
                
                if not visited[new_node - 1]:
                    visited[new_node-1] = True
                    q.append(new_node)
                    answer += 1
        
    bfs(1)
    return answer

if __name__ == '__main__':
    result = solution(N, connected, graph)
    print(result)