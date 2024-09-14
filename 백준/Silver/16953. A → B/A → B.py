from collections import deque

a, b = map(int, input().split())

def solution(a, b):
    count = 1
    q = deque()
    q.append(a)
    visited = set()
    child = []
    while q:
        num = q.popleft()
        
        if num == b:
            return count
        
        arr = [2*num, int(str(num)+"1")]
 
        for elem in arr:
            if elem > b:
                continue
            if elem in visited:
                continue

            visited.add(elem)
            child.append(elem)

        if len(q) == 0:
            q.extend(child)
            count += 1
            child = []

    return -1

if __name__ == "__main__":
    result = solution(a, b)
    print(result)