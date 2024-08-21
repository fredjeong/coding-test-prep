def solution(k, dungeons):
    global visited, answer
    answer = 0
    visited = [False for _ in range(len(dungeons))]
    dfs(k, 0, dungeons)
    return answer

def dfs(k, count, dungeons):
    global answer
    if count > answer:
        answer = count
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k-dungeons[i][1], count+1, dungeons)
            visited[i] = False
        