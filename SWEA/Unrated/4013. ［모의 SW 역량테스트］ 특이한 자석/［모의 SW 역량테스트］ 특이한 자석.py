from collections import deque

T = int(input())

for test_case in range(1, T+1):
    k = int(input())

    magnets = deque()
    for _ in range(4):
        magnets.append(deque(map(int, input().split())))

    # 자석을 회전시키는 정보: 1일 경우 시계방향, -1일 경우 반시계방향
    for _ in range(k):
        magnet_num, magnet_dir = map(int, input().split())
        magnet_num -= 1 # 자석 번호가 0부터 시작하도록 조정

        arr = []

        visited = [False for _ in range(4)]
        q = deque()
        q.append((magnet_num, magnet_dir))

        while q:
            idx, direction = q.popleft()
            visited[idx] = True
            arr.append((idx, direction))
            if idx != 3:
                if magnets[idx][2] != magnets[idx+1][-2] and not visited[idx+1]:
                    q.append((idx+1, direction*(-1)))
            if idx != 0:
                if magnets[idx][-2] != magnets[idx-1][2] and not visited[idx-1]:
                    q.append((idx-1, direction*(-1)))

        for i, direction in arr:
            magnets[i].rotate(direction)

    score = 0
    if magnets[0][0]:
        score += 1
    if magnets[1][0]:
        score += 2
    if magnets[2][0]:
        score += 4
    if magnets[3][0]:
        score += 8

    print(f"#{test_case} {score}")