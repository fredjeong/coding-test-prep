import sys
input = sys.stdin.readline

from collections import deque

class Problem():
    def __init__(self):
        self.original_a = input().strip()
        self.original_b = input().strip()
        self.original_a, self.original_b = sorted([self.original_a, self.original_b], key=lambda x:-len(x))

    def run(self):
        # 짧은 애를 놔두고 긴 애를 움직여가면서
        a = self.original_a
        b = self.original_b
        a = deque(a)
        length_a = len(a)
        length_b = len(b)
        count = 0
        while a:
            temp = "".join(a)
            do_break = False
            for idx in range(min(len(temp), length_b)):
                # 둘 다 이라면 불가능
                if temp[idx] == "2" and b[idx] == "2":
                    do_break = True
                    break
            if do_break:
                count += 1
                a.popleft()
            else:
                break
        if count <= length_a - length_b:
            return length_a
        else:
            return count + length_b

    def backwards_run(self):
        # 짧은 애를 놔두고 긴 애를 움직여가면서
        a = self.original_a
        b = self.original_b
        new_a = ""
        new_b = ""
        for i in range(len(a)):
            new_a = a[i] + new_a
        for i in range(len(b)):
            new_b = b[i] + new_b
        a = new_a
        a = deque(a)
        b = new_b
        length_a = len(a)
        length_b = len(b)
        count = 0
        while a:
            temp = "".join(a)
            do_break = False
            for idx in range(min(len(temp), length_b)):
                # 둘 다 이라면 불가능
                if temp[idx] == "2" and b[idx] == "2":
                    do_break = True
                    break
            if do_break:
                count += 1
                a.popleft()
            else:
                break
        if count <= length_a - length_b:
            return length_a
        else:
            return count + length_b

def main():
    instance = Problem()
    forward = instance.run()
    backward = instance.backwards_run()
    print(min(forward, backward))

if __name__ == "__main__":
    main()