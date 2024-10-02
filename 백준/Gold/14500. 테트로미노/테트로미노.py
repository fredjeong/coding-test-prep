import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

maximum = 0

"""
OOOO
"""
for i in range(n):
    for j in range(m-3):
        if j==m-4:
            target = sum(board[i][j:])
        else:
            target = sum(board[i][j:j+4])
        if target > maximum:
            maximum = target

"""
O
O
O
O
"""
for i in range(n-3):
    for j in range(m):
        target = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j]
        if target > maximum:
            maximum = target

"""
OO
OO
"""
for i in range(n-1):
    for j in range(m-1):
        target = board[i][j] + board[i][j+1] + board[i+1][j] + board[i+1][j+1]
        if target > maximum:
            maximum = target

"""
O    O  O   OO   O  OO  O    O
OO  OO  O    O   O  O   OO  OO
O    O  OO   O  OO  O    O  O
"""
for i in range(n-2):
    for j in range(m-1):
        target = board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+2][j]
        if target > maximum:
            maximum = target
        target = board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+2][j+1]
        if target > maximum:
            maximum = target
        target = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+2][j+1]
        if target > maximum:
            maximum = target
        target = board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+2][j+1]
        if target > maximum:
            maximum = target
        target = board[i][j+1] + board[i+1][j+1] + board[i+2][j] + board[i+2][j+1]
        if target > maximum:
            maximum = target
        target = board[i][j+1] + board[i][j] + board[i+1][j] + board[i+2][j]
        if target > maximum:
            maximum = target
        target = board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+2][j+1]
        if target > maximum:
            maximum = target
        target = board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+2][j]
        if target > maximum:
            maximum = target
        
"""
OOO  O  OOO   O O   OOO  OO OO
 O  OOO O   OOO OOO   O OO   OO
"""
for i in range(n-1):
    for j in range(m-2):
        target = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+1]
        if target > maximum:
            maximum = target
        target = board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2]
        if target > maximum:
            maximum = target
        target = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j]
        if target > maximum:
            maximum = target
        target = board[i][j+2] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2]
        if target > maximum:
            maximum = target
        target = board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2]
        if target > maximum:
            maximum = target
        target = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+2]
        if target > maximum:
            maximum = target
        target = board[i][j+1] + board[i][j+2] + board[i+1][j] + board[i+1][j+1]
        if target > maximum:
            maximum = target
        target = board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+1][j+2]
        if target > maximum:
            maximum = target

print(maximum)