from collections import deque

arr = deque(list(map(int, input().split())))
for i in range(len(arr)):
    arr[i] *= 0.01
N = 8

prob = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i < j:
            prob[i][j] = arr.popleft()

for i in range(N):
    for j in range(N):
        if j < i:
            prob[i][j] = 1-prob[j][i]

# 각 선수가 1라운드 통과할 확률
round_1 = []
for i in range(0, N, 2):
    round_1.append(prob[i][i+1])
    round_1.append(1 - prob[i][i+1])

# 각 선수가 2라운드 통과할 확률
round_2 = []
for i in range(N):
    if i//4 == 0:
        if i//2 == 0:
            round_2.append(round_1[i]*(round_1[2]*prob[i][2] + round_1[3]*prob[i][3]))
        elif i//2 == 1:
            round_2.append(round_1[i]*(round_1[0]*prob[i][0] + round_1[1]*prob[i][1]))
    elif i//4 == 1:
        if (i-4)//2 == 0:
            round_2.append(round_1[i]*(round_1[6]*prob[i][6] + round_1[7]*prob[i][7]))
        elif (i-4)//2 == 1:
            round_2.append(round_1[i]*(round_1[4]*prob[i][4] + round_1[5]*prob[i][5]))

# 각 선수가 3라운드 통과할 확률
round_3 = []
for i in range(N):
    if i//4 == 0:
        round_3.append(round_2[i]*(round_2[4]*prob[i][4] + round_2[5]*prob[i][5] 
                       + round_2[6]*prob[i][6] + round_2[7]*prob[i][7]))
    elif i//4 == 1:
        round_3.append(round_2[i]*(round_2[0]*prob[i][0] + round_2[1]*prob[i][1] 
                       + round_2[2]*prob[i][2] + round_2[3]*prob[i][3]))

print(" ".join(map(str, round_3)))