import sys
input = sys.stdin.readline

class Problem():
    def __init__(self):
        self.n = int(input())
        self.answer = ""

    def run(self):
        history = {}
        rollback_history = {}
        for _ in range(self.n):
            # 실행할 명령 저장하고 실행
            order, content, time = input().split()

            if order == "type":
                history[int(time)] = content
                self.answer += content
            else:
                # 일단 박제하고 저장
                rollback_history[int(time)] = self.answer
                history[int(time)] = content

                temp = [sec for sec in history.keys() if int(time) - int(content) <= sec < int(time)]
                temp = sorted(temp, reverse=True)

                for sec in temp:
                    # 되돌리기를 되돌리기
                    if history[sec].isdigit():
                        self.answer = rollback_history[sec]

                    # 마지막 글자 지우기
                    else:
                        self.answer = self.answer[:-1]
        print(self.answer)

def main():
    instance = Problem()
    instance.run()

if __name__ == "__main__":
    main()