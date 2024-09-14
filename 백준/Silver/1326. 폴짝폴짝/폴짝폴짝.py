from collections import deque

N = int(input())
arr = list(map(abs, map(int, input().split())))
A, K = map(int, input().split())

def solution(N, arr, A, K):
    if A == K:
        return 0
    
    def bfs(N, arr, A, K):
        count = 0
        if (K - A) % arr[A-1] == 0:
            return 1
        q = deque()
        q.append(A)
        visited = set()
        temp = []
        while q:
            cur = q.popleft()
            if cur == K:
                return count

            # 앞으로 가는 경우
            if cur+arr[cur-1] <= N:
                for pos in range(cur+arr[cur-1], N+1, arr[cur-1]):
                    if pos in visited:
                        continue
                    visited.add(pos)
                    temp.append(pos)
                
            # 뒤로 가는 경우
            if cur-arr[cur-1] >= 1:
                for pos in range(cur-arr[cur-1], 0, -arr[cur-1]):
                    if pos in visited:
                        continue
                    visited.add(pos)
                    temp.append(pos)
            
            if len(q) == 0:
                q.extend(temp)
                temp = []
                count += 1

        return -1
    
    return bfs(N, arr, A, K)

if __name__ == "__main__":
    result = solution(N, arr, A, K)
    print(result)