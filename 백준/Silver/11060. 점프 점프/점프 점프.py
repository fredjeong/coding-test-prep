from collections import deque

N = int(input())
arr = list(map(int, input().split()))

def solution(N, arr):
    
    def bfs(N, arr):
        start = 0
        q = deque()
        q.append(start)

        length = len(arr)
        visited = []
        count = 0
        temp = []
        while q:
            pos = q.popleft()
            if pos == length-1:
                return count

            for step in range(1, arr[pos]+1):
                new_pos = pos + step
                if new_pos >= length:
                    continue
                if new_pos not in visited:
                    visited.append(new_pos)
                    temp.append(new_pos)
            
            if len(q) == 0:
                q.extend(temp)
                count += 1
                temp = []
        
        return -1
    
    return bfs(N, arr)
    

if __name__ == "__main__":
    result = solution(N, arr)
    print(result)