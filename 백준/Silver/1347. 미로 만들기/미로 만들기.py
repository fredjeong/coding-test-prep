N = int(input())
arr = str(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

direction = 0

x = 0
y = 0

x_arr = []
y_arr = []

x_arr.append(x)
y_arr.append(y)

for i in range(N):
    if arr[i] == "R":
        direction += 1
        if direction >= 4:
            direction = direction % 4
    elif arr[i] == "L":
        direction -= 1
        if direction < 0:
            direction += 4
    elif arr[i] == "F":
        #print(direction)
        x += dx[direction]
        y += dy[direction]
        x_arr.append(x)
        y_arr.append(y)

x_min = min(x_arr)
x_arr_length = len(x_arr)
if x_min < 0:
    for i in range(x_arr_length):
        x_arr[i] -= x_min
y_min = min(y_arr)
y_arr_length = len(y_arr)
if y_min < 0:
    for i in range(y_arr_length):
        y_arr[i] -= y_min

rows = max(x_arr) - min(x_arr) + 1
cols = max(y_arr) - min(y_arr) + 1
board = [["#" for _ in range(cols)] for _ in range(rows)] 
for i in range(len(x_arr)):
    board[x_arr[i]][y_arr[i]] = "."

for i in range(rows):
    print("".join(map(str,board[i])))