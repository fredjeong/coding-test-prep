import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

def bfs(board):
    dic = {}
    dic[0] = 0
    dic[1] = 0    

    q = deque()
    q.append(board)

    while q:
        arr = q.popleft()
        length = len(arr)
        init = arr[0][0]
        
        if length == 1:
            dic[init] += 1
            continue
        
        do_separate = False
        for i in range(length):
            for j in range(length):
                if i==0 and j==0:
                    continue
                else:
                    if arr[i][j] != init:
                        do_separate = True
                        break
            if do_separate == True:
                break
        if do_separate == False:
            dic[init] += 1
            continue

        temp_1 = []
        temp_2 = []
        temp_3 = []
        temp_4 = []
        for i in range(length):
            if i < length//2:
                temp_1.append(arr[i][:length//2])
                temp_2.append(arr[i][length//2:])
            else:
                temp_3.append(arr[i][:length//2])
                temp_4.append(arr[i][length//2:])

        q.append(temp_1)
        q.append(temp_2)
        q.append(temp_3)
        q.append(temp_4)

    return dic[0], dic[1]

white, blue = bfs(board)
print(white)
print(blue)