# dfs 재귀함수 정의
def dfs(string, x, y):
    string += board[x][y]

    # 7자리가 찼다면 결과를 집합에 추가하고 종료
    if len(string) == 7:
        s.add(string)
        return

    # 동서남북 방향
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        # 격자 밖인 경우 무시
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            continue

        # 재귀함수 실행
        dfs(string, nx, ny)

T = int(input())

for test_case in range(1, T+1):
    board = []
    for _ in range(4):
        board.append(list(input().split()))

    # 서로 다른 7자리 숫자의 개수 저장
    s = set()

    # 방향 정의
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 총 7번 방문하며 각 칸에 적혀있는 숫자를 차례대로 이어 붙이기
    for i in range(4):
        for j in range(4):
            # 재귀함수 실행
            dfs("", i, j)

    print(f"#{test_case} {len(s)}")
