def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    answer[0][0] = 1
    check = [[True for _ in range(n)] for _ in range(n)]
    check[0][0] = False
    x = 0
    y = 0
    direction = "right"
    count = 1
    while count < n ** 2:
        if direction == "right":
            if x + 1 < n:
                if check[y][x+1] == True:
                    x += 1
                    count += 1
                    answer[y][x] = count
                    check[y][x] = False
                else: 
                    direction = "down"
            else:
                direction = "down"
        elif direction == "down":
            if y + 1 < n:
                if check[y+1][x] == True:
                    y += 1
                    count += 1
                    answer[y][x] = count
                    check[y][x] = False
                else:
                    direction = "left"
            else:
                direction = "left"
        elif direction == "left":
            if x - 1 >= 0:
                if check[y][x-1] == True:
                    x -= 1
                    count += 1
                    answer[y][x] = count
                    check[y][x] = False
                else:
                    direction = "up"
            else:
                direction = "up"
        elif direction == "up":
            if y - 1 > 0:
                if check[y-1][x] == True:
                    y -= 1
                    count += 1
                    answer[y][x] = count
                    check[y][x] = False
                else:
                    direction = "right"
            else:
                direction = "right"
    return answer
        