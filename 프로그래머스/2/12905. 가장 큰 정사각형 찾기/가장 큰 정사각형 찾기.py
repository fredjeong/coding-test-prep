def solution(board):
    # dp 준비
    dp = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    dp[0] = board[0]
    for i in range(1,len(board)):
        dp[i][0] = board[i][0]
    
    # 2중 포문으로 연산
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    
    # 최대 넓이 구하기
    answer = 0
    for i in range(len(board)):
        temp = max(dp[i])
        answer = max(answer, temp)
    
    return answer**2

#def solution(board):
#    answer = 0
#    length = 1
#    
#    for row in range(len(board)):
#        if row + length - 1 >= len(board):
#            break
#        for col in range(len(board[0])):
#            # 만약 현재 row, col에서 length만큼의 정사각형을 만들 수 없다면 패스
#            if col + length - 1 >= len(board[0]):
#                break
#            # 1인 점을 찾고
#            if board[row][col] == 1:
#                while True:
#                    if row + length - 1 >= len(board) or col + length - 1 >= len(board[0]):
#                        break
#                    
#                    is_break = 0
#                    # 오른쪽, 아래, 대각선"까지가" 모두 1인지 확인
#                    for temp_row in range(row, row+length):
#                        if 0 in board[temp_row][col:col+length]:
#                            is_break = 1
#                            break
#                    
#                    if is_break == 1:
#                        break
#                    
#                    answer = length**2
#                    length += 1
#
#    return answer