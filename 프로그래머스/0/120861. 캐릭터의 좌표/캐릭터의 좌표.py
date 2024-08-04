def solution(keyinput, board):
    position = [0,0]
    for key in keyinput:
        if key == "up":
            if position[1] != (board[1] - 1)/2:
                position[1] += 1
            else:
                pass
        elif key == "down":
            if position[1] != -(board[1] - 1)/2:
                position[1] -= 1
            else:
                pass
        elif key == "right":
            if position[0] != (board[0] - 1)/2:
                position[0] += 1
            else:
                pass
        elif key == "left":
            if position[0] != -(board[0] - 1)/2:
                position[0] -= 1
            else:
                pass
    return position
