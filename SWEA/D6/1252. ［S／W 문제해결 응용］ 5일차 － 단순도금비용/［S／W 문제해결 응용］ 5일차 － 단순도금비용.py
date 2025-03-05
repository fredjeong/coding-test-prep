import heapq

def get_count(x, y, size):
    cnt = 0
    for sub_x in range(size):
        for sub_y in range(size):
            nx = x + sub_x
            ny = y + sub_y

            if board[nx][ny]:
                cnt += 1
    return cnt

T = int(input())

for test_case in range(1, T+1):
    s = int(input()) # 금속판의 한 변의 길이
    n = int(input()) # 손상된 부분의 개수
    arr = list(map(int, input().split()))

    board = [[0 for _ in range(s)] for _ in range(s)]

    for i in range(n):
        board[arr[2*i]-1][arr[2*i+1]-1] = 1

    # 임계값
    thresholds = [0, 1, 2, 5]

    q = []
    heapq.heapify(q)

    for size in range(3, 0, -1):
        for x in range(s-size+1):
            for y in range(s-size+1):
                # 좌상단 좌표: (x, y)
                # 범위 안에 있는 방문하지 않은 손상 개수
                cnt = get_count(x, y, size)

                if cnt > 0 and cnt >= thresholds[size]:
                    heapq.heappush(q, (-cnt, -size, x, y))

    total = 0
    result = []

    while q:
        cnt, size, x, y = heapq.heappop(q)

        cnt = -cnt
        size = -size

        # 블록 개수 최신화
        new_cnt = get_count(x, y, size)

        if new_cnt == cnt:
            # 방문처리
            for sub_x in range(size):
                for sub_y in range(size):
                    nx = x + sub_x
                    ny = y + sub_y
                    board[nx][ny] = 0
                    
            result.append([x+1, y+1, size])
            total += 1

        elif new_cnt > 0:
            for new_size in range(size, 0, -1):
                new_new_cnt = get_count(x, y, new_size)
                if new_new_cnt > 0 and new_new_cnt >= thresholds[new_size]:
                    heapq.heappush(q, (-new_new_cnt, -new_size, x, y))

    for i in range(len(result)):
        result[i] = " ".join(map(str, result[i]))

    print(f"#{test_case} {total} {' '.join(map(str, result))}")