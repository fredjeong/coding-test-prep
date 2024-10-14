import sys
input = sys.stdin.readline

class Problem():
    def __init__(self):
        self.n = int(input())
        self.board = [list(map(int, input().split())) for _ in range(self.n)]
        self.pos = [0, 1]
        # direction: right, down, diagonal 이렇게 세 개
        self.count = 0
        self.impossible = False

    def dfs(self, pos, direction):
        if self.board[self.n - 1][self.n - 1] == 1:
            self.impossible = True
            print(0)
            return

        if pos == [self.n - 1, self.n - 1]:
            self.count += 1
            return

        right_pos = [pos[0], pos[1] + 1]
        down_pos = [pos[0] + 1, pos[1]]
        diagonal_pos = [pos[0] + 1, pos[1] + 1]

        if right_pos[1] < self.n:
            if self.board[right_pos[0]][right_pos[1]] != 1:
                if direction == 'right' or direction == 'diagonal':
                    self.dfs(right_pos, 'right')
        if down_pos[0] < self.n:
            if self.board[down_pos[0]][down_pos[1]] != 1:
                if direction == 'down' or direction == 'diagonal':
                    self.dfs(down_pos, 'down')

        if diagonal_pos[0] < self.n and diagonal_pos[1] < self.n:
            if self.board[pos[0] + 1][pos[1]] != 1 and self.board[pos[0] + 1][pos[1] + 1] != 1 and self.board[pos[0]][
                pos[1] + 1] != 1:
                self.dfs(diagonal_pos, 'diagonal')

def main():
    instance = Problem()
    instance.dfs([0, 1], 'right')
    if not instance.impossible:
        print(instance.count)

if __name__ == "__main__":
    main()