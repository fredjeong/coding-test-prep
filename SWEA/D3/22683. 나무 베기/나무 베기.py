from collections import deque

T = int(input())

for test_case in range(1, T+1):
    n, k = map(int, input().split())
    
    # 필드의 정보
    board = []
    for row in range(n):
        arr = list(input())
        for col in range(n):
            # 초기 위치 파악
            if arr[col] == "X":
                x_init = row
                y_init = col
        board.append(arr)
    
    """
    앞으로 이동
    왼쪽으로 90도 회전
    오른쪽으로 90도 회전
    """

    # 북 동 남 서 
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    min_cnt = 1e9

    def recursion(x, y, cnt, direction, cut_cnt_left, history):
        global min_cnt

        # 종료 조건 1: 현재까지 최솟값보다 cnt가 클 경우
        if cnt >= min_cnt:
            return
        # 종료 조건 2: Y 지점에 도달했을 경우
        if board[x][y] == "Y":
            min_cnt = min(min_cnt, cnt)
            return
        
        # 4방향 모두 고려하는 것이 아니라 현재 방향 기준 +-1까지만 가능
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 격자를 벗어난 경우는 고려하지 않는다
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            # 이미 방문한 지점은 고려하지 않는다
            if (nx, ny) in history:
                continue
            
            # 나무가 있어 이동이 불가능한 경우
            if board[nx][ny] == "T":
                # cut_cnt_left가 0이라면 고려하지 않는다
                if not cut_cnt_left:
                    continue
                else:
                    # 나무를 베고 지나가는 경우
                    if direction == i:
                        recursion(nx, ny, cnt+1, i, cut_cnt_left-1, history | {(nx ,ny)})
                    elif abs(direction - i) == 2:
                        recursion(nx, ny, cnt+3, i, cut_cnt_left-1, history | {(nx ,ny)})
                    else:
                        recursion(nx, ny, cnt+2, i, cut_cnt_left-1, history | {(nx ,ny)})

            # RC카가 이동 가능한 땅 / RC카를 이동시키고자 하는 위치
            else:
                if direction == i:
                    recursion(nx, ny, cnt+1, i, cut_cnt_left, history | {(nx ,ny)})
                elif abs(direction - i) == 2:
                    recursion(nx, ny, cnt+3, i, cut_cnt_left, history | {(nx ,ny)})
                else:
                    recursion(nx, ny, cnt+2, i, cut_cnt_left, history | {(nx ,ny)})

    # 처음은 항상 북쪽을 바라보고 있음
    recursion(x_init, y_init, 0, 0, k, {(x_init, y_init)})


    if min_cnt == 1e9:
        min_cnt = -1

    print(f"#{test_case} {min_cnt}")