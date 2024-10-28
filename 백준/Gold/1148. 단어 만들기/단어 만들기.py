import sys
input = sys.stdin.readline

from collections import defaultdict, deque

class Problem():
    def __init__(self):
        self.words = []
        while True:
            word = input().strip()
            if word == "-":
                break
            dic = defaultdict(int)
            for character in word:
                dic[character] += 1
            self.words.append(dic)

        self.candidates = deque()
        while True:
            candidate = input().strip()
            if candidate == "#":
                break
            self.candidates.append(candidate)

    def run(self):
        # 보드판 불러오기
        candidate = self.candidates.popleft()

        count = {}
        for character in candidate:
            if character not in count:
                count[character] = 0

        dic = defaultdict(int)
        for character in candidate:
            dic[character] += 1

        # 각 글자가 가운데 왔을 때 정답의 개수가 몇 개 나오는지 조사
        for character in dic.keys():
            for word in self.words:
                # 가운데 글자를 포함하고 있지 않다면 고려하지 않는다
                if character not in word:
                    continue

                do_break = False
                for char in word.keys():
                    if char not in dic.keys():
                        do_break = True
                        break
                    if word[char] > dic[char]:
                        do_break = True
                        break
                if not do_break:
                    count[character] += 1

        min_count = min(count.values())
        max_count = max(count.values())

        min_arr = []
        max_arr = []

        for char in count:
            if count[char] == min_count:
                min_arr.append(char)
                continue
            if count[char] == max_count:
                max_arr.append(char)
                continue

        if not max_arr:
            print("".join(sorted(min_arr)), min_count, "".join(sorted(min_arr)), min_count)
        else:
            print("".join(sorted(min_arr)), min_count, "".join(sorted(max_arr)), max_count)

def main():
    instance = Problem()
    for _ in range(len(instance.candidates)):
        instance.run()

if __name__ == "__main__":
    main()