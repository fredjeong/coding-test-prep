def solution(board, moves):
    answer = 0
    basket = [0]
    # move - 1이 board에서 선택할 열의 인덱스가 된다
    for i in moves:
        row = 0
        column = i - 1
        while row != len(board):
            if board[row][column] == 0:
                row += 1
            else:
                new = board[row][column]
                # 인형을 뽑는 순서대로 바구니에 담고, 만약 바구니의 바로 직전 인형과 같다면 터뜨린다
                if new == basket[-1]:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(new)
                board[row][column] = 0
                break
    return answer