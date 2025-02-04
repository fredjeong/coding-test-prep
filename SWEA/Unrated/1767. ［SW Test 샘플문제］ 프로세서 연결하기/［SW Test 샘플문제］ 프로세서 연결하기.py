T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    # 한 개의 셀에는 한 개의 코어 혹은 한 개의 전선이 올 수 있다
    visited_ = [[False for _ in range(n)] for _ in range(n)]

    arr = []
    connected = 0
    for row in range(n):
        for col in range(n):
            if board[row][col]:
                visited_[row][col] = True
                if row == 0 or row == n - 1 or col == 0 or col == n - 1:
                    connected += 1
                if row != 0 and row != n - 1 and col != 0 and col != n - 1:
                    arr.append((row, col))

    max_core = connected
    min_wire = 0

    def recursion(idx, num_connected, wire_length, _visited_):
        global max_core, min_wire

        # 남은걸 다 더해도 max_core보다 작으면 리턴
        # if num_connected + n - idx < max_core:
        #     return

        if num_connected > max_core:
            max_core = num_connected
            min_wire = wire_length

        elif num_connected == max_core:
            min_wire = min(min_wire, wire_length)

        # arr의 idx번째 좌표 시도해보기
        if idx == len(arr):
            return

        # 연결하지 않거나
        recursion(idx + 1, num_connected, wire_length, _visited_)

        # 상하좌우 연결 시 이동 방향에 visited가 모두 False여야 함
        x, y = arr[idx]

        # 상
        if set([_visited_[i][y] for i in range(x + 1, n)]) == {0}:
            visited = []
            for row_ in range(n):
                visited.append(_visited_[row_][:])
            for i_ in range(x + 1, n):
                visited[i_][y] = True
            recursion(idx + 1, num_connected + 1, wire_length + n - x - 1, visited)

        # 하
        if set([_visited_[i][y] for i in range(x)]) == {0}:
            visited = []
            for row_ in range(n):
                visited.append(_visited_[row_][:])
            for i_ in range(x):
                visited[i_][y] = True
            recursion(idx + 1, num_connected + 1, wire_length + x, visited)

        # 좌
        if set([_visited_[x][i] for i in range(y)]) == {0}:
            visited = []
            for row_ in range(n):
                visited.append(_visited_[row_][:])
            for i_ in range(y):
                visited[x][i_] = True
            recursion(idx + 1, num_connected + 1, wire_length + y, visited)

        # 우
        if set([_visited_[x][i] for i in range(y + 1, n)]) == {0}:
            visited = []
            for row_ in range(n):
                visited.append(_visited_[row_][:])
            for i_ in range(y + 1, n):
                visited[x][i_] = True
            recursion(idx + 1, num_connected + 1, wire_length + n - y - 1, visited)

    recursion(0, connected, 0, visited_)

    print(f"#{test_case} {min_wire}")