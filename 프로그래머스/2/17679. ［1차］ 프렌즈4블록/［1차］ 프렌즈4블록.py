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
    
#
#
#
#    
#    # 캐릭터를 기준으로 탐색하는 것이 아니라 좌표를 기준으로 탐색해야 함 (CNN처럼)
#    # row i, column j에 대해서 [i,j], [i+1,j], [i,j+1], [i+1, j+1]이 모두 같은지 보기
#    # 칸들을 지울지 여부를 판별하는 영행렬을 만들고 매번 초기화
#
#    board = [[board[i][j] for j in range(n)] for i in range(m)]
#    
#    answer = 0
#    while m < n:
#        visited = [[False for _ in range(n)] for _ in range(m)]
#        for i in range(m-1):
#            for j in range(n-1):
#                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
#                    visited[i][j] = True
#                    visited[i][j+1] = True
#                    visited[i+1][j] = True
#                    visited[i+1][j+1] = True
#        if visited == [[False for _ in range(n)] for _ in range(m)]:
#            break
#        # while문 벗어나는 조건
#        # 지울지 여부를 판별하는 영행렬이 그대로면 반복문 종료
#        print(visited)
#        print(True in visited)
#        counter = 0
#        if True not in [visited[i][j] for i in range(m)]:
#            counter += 1
#        if counter == m:
#            break
#        # True가 있다면 해당하는 부분들은 모두 특수문자로 바꿔주고 한칸씩 아래로 내려야 한다
#        else:
#            
#            for i in range(m):
#                for j in range(n):
#                    if visited[i][j] == True:
#                        board[i][j] = "0" # isdigit()을 사용할 수 있도록
#            
#            for col in range(n):
#                zeros = 0
#                temp = ""
#                newtemp = ""
#                for row in range(m):
#                    if board[row][col] == "0":
#                        zeros += 1
#                    elif board[row][col].isalpha():
#                        temp += board[row][col]
#                answer += 1
#                newtemp = "1" * (m - len(temp)) + temp
#                for row in range(m):
#                    board[row][col] = newtemp[row]
#    return answer