def solution(m, n, board):
    answer = 0
    board = [[board[i][j] for j in range(n)] for i in range(m)]
    
    while True:
        # 4개짜리가 있는지 확인
        check = [[False for _ in range(n)] for _ in range(m)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        for row in range(m-1):
            for col in range(n-1):
                if board[row][col] == board[row][col+1] == board[row+1][col] == board[row+1][col+1] and board[row][col].isalpha():
                    visited[row][col] = True
                    visited[row][col+1] = True
                    visited[row+1][col] = True
                    visited[row+1][col+1] = True
        if visited == check:
            break

        # 블록 지우기
        for row in range(m):
            for col in range(n):
                if visited[row][col] == True:
                    board[row][col] = "0"
                    answer += 1

        # 블록 아래로 내리기
        for col in range(n):
            temp = ""
            
            for row in range(m):
                temp += board[row][col]
                temp = temp.replace("0", "")
                temp = temp.replace("1", "")
            new_temp = "1" * (m - len(temp)) + temp
            
            for row in range(m):
                board[row][col] = new_temp[row]
                
    return answer