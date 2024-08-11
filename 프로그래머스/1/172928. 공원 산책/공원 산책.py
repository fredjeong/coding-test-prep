def solution(park, routes):
    height = len(park)
    width = len(park[0])
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                start = [i, j]
                break
    row = start[0]
    col = start[1]
    
    for route in routes:
        route = route.split(" ")
        direction, distance = route[0], int(route[1])
        if direction == "E":
            if col + distance < len(park[0]):
                for i in range(1, distance + 1):
                    count = i
                    if park[row][col + i] == "X":
                        count = 0
                        break
                if count == distance:
                    col += distance
        elif direction == "W":
            if col - distance >= 0:
                for i in range(1, distance + 1):
                    count = i
                    if park[row][col- i] == "X":
                        count = 0
                        break
                if count == distance:
                    col -= distance
        elif direction == "S":
            if row + distance < len(park):
                for i in range(1, distance + 1):
                    count = i
                    if park[row + i][col] == "X":
                        count = 0
                        break
                if count == distance:
                    row += distance
        elif direction == "N":
            if row - distance >= 0:
                for i in range(1, distance + 1):
                    count = i
                    if park[row - i][col] == "X":
                        count = 0
                        break
                if count == distance:
                    row -= distance
    answer = [row, col]
    return answer