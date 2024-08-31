def solution(arr):
    answer = [0, 0]
    
    def dfs(a, b, l):
        init = arr[a][b]
        
        for i in range(a, a + l):
            for j in range(b, b + l):
                if arr[i][j] != init:
                    l //= 2
                    dfs(a, b, l)
                    dfs(a, b + l, l)
                    dfs(a + l, b, l)
                    dfs(a + l, b + l, l)
                    return
        
        answer[init] += 1
    
    dfs(0, 0, len(arr))
    
    return answer