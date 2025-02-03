from collections import deque, defaultdict

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    q = deque()
    for _ in range(n):
        y, x, direction, energy = map(int, input().split())
        q.append((-x, y, direction, energy))

    # 0: 상, 1: 하, 2: 좌, 3: 우
    dx = [-0.5, 0.5, 0, 0]
    dy = [0, 0, -0.5, 0.5]

    # 원자들이 소멸되면서 방출하는 에너지의 총합
    total = 0
    timestep = 0
    while True:
        dic = defaultdict(list)

        # 동시에 이동 시작
        while q:
            x, y, direction, energy = q.popleft()

            nx = x + dx[direction]
            ny = y + dy[direction]

            if nx < -1000 or nx > 1000 or ny < -1000 or ny >= 1000:
                continue
            dic[(nx, ny)].append((direction, energy))

        for coordinates in dic:
            atoms = dic[coordinates]
            if len(atoms) > 1:
                for atom in atoms:
                    total += atom[1]
            else:
                x, y = coordinates
                for atom in atoms:
                    q.append((x, y, atom[0], atom[1]))
        if not q:
            break

    print(f"#{test_case} {total}")
