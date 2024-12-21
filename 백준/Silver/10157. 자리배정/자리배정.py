import sys

input = sys.stdin.readline

r, c = map(int, input().split())
k = int(input())

if k > c*r:
    print(0)
else:
    taken = [[False for _ in range(r)] for _ in range(c)]
    count = 1

    col = 0
    row = 0

    direction = 0 
    
    while count < k:
        taken[col][row] = True

        if direction == 0:
            if col + 1 >= c or taken[col+1][row]:
                direction = 1
                row += 1
            else:
                col += 1

        elif direction == 1:
            if row + 1 >= r or taken[col][row+1]:
                direction = 2
                col -= 1
            else:
                row += 1

        elif direction == 2:
            if col - 1 < 0 or taken[col-1][row]:
                direction = 3
                row -= 1
            else:
                col -= 1

        elif direction == 3:
            if row - 1 < 0 or taken[col][row-1]:
                direction = 0
                col += 1
            else:
                row -= 1

        count += 1

    print(row+1, col+1)