from collections import deque

N = int(input()) # 총 인원 수
A, B = map(int, input().split())
T = int(input())
graph = [list(map(int, input().split())) for _ in range(T)]

def solution(N, A, B, T, graph):

    def bfs(N, A, B, T, graph):
        visited = [False for _ in range(N)]
        
        q = deque()
        q.append(A)
        count = 0
        temp = []
        while q:
            num = q.popleft()
            if num == B:
                return count

            # 자식 노드
            for i in range(len(graph)):
                if graph[i][0] == num:
                    if visited[graph[i][1]-1] == False:
                        visited[graph[i][1]-1] = True
                        temp.append(graph[i][1])
                elif graph[i][1] == num:
                    if visited[graph[i][0]-1] == False:
                        visited[graph[i][0]-1] = True
                        temp.append(graph[i][0])

            if len(q) == 0:
                q.extend(temp)
                temp = []
                count += 1

        return -1

    return bfs(N, A, B, T, graph)

if __name__ == "__main__":
    result = solution(N, A, B, T, graph)
    print(result)