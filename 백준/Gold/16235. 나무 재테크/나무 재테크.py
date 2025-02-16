import sys
from collections import defaultdict, deque

input = sys.stdin.readline

"""
보드의 크기: n*n (같은 칸에 여러 나무가 있을 수 있음)
나무의 개수: m 
"""
n, m, k = map(int, input().split())

A = [] # 양분
for _ in range(n):
    A.append(list(map(int, input().split())))

# 나무의 위치와 나이
trees = {}
for _ in range(m):
    x, y, age = map(int, input().split())
    # r, c는 1부터 시작한다
    trees[(x-1, y-1)] = deque([age])

# 가장 처음에 양분은 모든 칸에 5만큼 들어있다
nutrition = [[5 for _ in range(n)] for _ in range(n)]

# 방향 탐색
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

# 나무는 k년 동안 사계절을 보내며 특정 과정을 반복함
for _ in range(k):
    new_trees = defaultdict(int)

    for coordinates in trees:
        x, y = coordinates

        # 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다
        ages = trees[coordinates]

        ages_survived = deque()
        num_reproduce_trees = 0

        while ages:
            age = ages.popleft()

            # 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다
            if age > nutrition[x][y]:
                ages.appendleft(age)
                break

            # 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가
            nutrition[x][y] -= age
            age += 1

            ages_survived.append(age)
            if age % 5 == 0:
                num_reproduce_trees += 1

        # 인접한 8개의 칸에 나이가 1인 나무가 생긴다
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            # 땅을 벗어나는 칸에는 나무가 생기지 않는다
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            new_trees[(nx, ny)] += num_reproduce_trees

        trees[coordinates] = ages_survived

        # 봄에 죽은 나무는 양분으로 변한다
        # 각각의 죽은 나무마다 나이를 2로 나눈 몫이 나무가 있던 칸에 양분으로 추가된다
        for dead_tree_age in ages:
            nutrition[x][y] += dead_tree_age // 2

    for new_tree in new_trees:
        if new_tree not in trees:
            trees[new_tree] = deque()
        for _ in range(new_trees[new_tree]):
            trees[new_tree].appendleft(1)

    # 겨울
    # 각 칸에 양분이 추가된다
    for i in range(n):
        for j in range(n):
            nutrition[i][j] += A[i][j]

# 살아남은 나무의 개수 구하기
cnt = 0
for coordinates in trees:
    cnt += len(trees[coordinates])

print(cnt)