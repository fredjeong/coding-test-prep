def solution(n):
    answer = []
    # 직사각형 모양이라고 생각하자
    visited = [[0 for j in range(i+1)] for i in range(n)]
    
    total_count = 0
    for i in range(1,n+1):
        total_count += i
    
    counter = 1
    row = -1
    col = 0
    if n == 1:
        return [1]
    while counter <= total_count:
        # 1.첫 번째 column을 모두 돌고
        while True:
            row += 1
            if visited[row][col] != 0:
                row -= 1
                break
            visited[row][col] = counter
            counter += 1
            if row == n-1:
                break
            
        # 2.마지막 row를 돌고
        while True:
            
            col += 1
            if visited[row][col] != 0:
                col -= 1
                break
            visited[row][col] = counter
            counter += 1
            if col == n-1:
                break

        # 3.위에 있는 row들의 맨 끝 column을 돌고
        while True:
            if visited[row-1][col-1] != 0:
                break
            row -= 1
            col -= 1
            visited[row][col] = counter
            counter += 1

    answer = []
    for i in range(len(visited)):
        for j in range(len(visited[i])):
            answer.append(visited[i][j])
    return answer