import sys
input = sys.stdin.readline

class Problem():
    def __init__(self):
        self.l, self.c = map(int, input().split())
        self.arr = list(input().strip().split())
        self.arr.sort()

    def recursion(self, history_, idx):
        history = history_[:]
        history.append(self.arr[idx])

        if len(history) == self.l:
            consonants = 0
            vowels = 0
            for character in history:
                if character in 'aeiou':
                    vowels += 1
                else:
                    consonants += 1

            if vowels < 1 or consonants < 2:
                return
            else:
                print("".join(history))
                return

        for new_idx in range(idx+1, len(self.arr)):
            self.recursion(history, new_idx)

def main():
    instance = Problem()
    for idx in range(len(instance.arr)):
        instance.recursion([], idx)

if __name__ == "__main__":
    main()