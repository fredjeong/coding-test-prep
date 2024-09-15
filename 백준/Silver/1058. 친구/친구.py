from collections import deque

N = int(input())
graph = [input().strip() for _ in range(N)]

num = [0 for _ in range(N)]

for i in range(N):      # row
    for j in range(i+1, N):  # col
        # 두 사람이 친구인 경우
        if graph[i][j] == "Y":
            num[i] += 1
            num[j] += 1
            continue
        # 두 사람이 친구가 아니지만
        # i와 친구이고 j와 친구인 k가 존재하면 된다
        for col in range(N): # 사람
            if col == i or col == j:
                continue
            if graph[col][i] == "Y" and graph[col][j] == "Y":
                num[i] += 1
                num[j] += 1
                break

print(max(num))
