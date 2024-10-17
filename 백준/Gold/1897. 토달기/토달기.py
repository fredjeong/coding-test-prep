import sys
input = sys.stdin.readline

from collections import defaultdict, deque

class Problem():
    def __init__(self):
        self.dic = defaultdict(list)
        self.d, self.word = input().split()
        for _ in range(int(self.d)):
            word = input().strip()
            self.dic[len(word)].append(word)
        self.visited = {}
        for key in self.dic.keys():
            self.visited[key] = [False for _ in range(len(self.dic[key]))]

    def run(self):
        q = deque()
        q.append((self.word, len(self.word)))

        max_word = self.word
        max_length = len(max_word)

        while q:
            word, length = q.popleft()

            if length > max_length:
                max_word = word
                max_length = length

            length += 1

            for idx in range(len(self.dic[length])):
                new_word = self.dic[length][idx]
                if self.visited[length][idx]:
                    continue

                if self.check(word, new_word, length):
                    q.append((new_word, length))
                    self.visited[length][idx] = True

        print(max_word)

    def check(self, word, new_word, length):
        for i in range(length):
            temp_1 = new_word[:i]
            temp_2 = new_word[i+1:]
            temp = temp_1 + temp_2
            if temp == word:
                return True

        return False

def main():
    instance = Problem()
    instance.run()

if __name__ == "__main__":
    main()