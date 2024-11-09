import sys
input = sys.stdin.readline

class Problem():
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.pages = set(map(int, input().split()))

    def run(self):
        # 인쇄하지 않거나
        # 새로 체크포인트를 만들어 인쇄를 시작하거나
        # 이전 체크포인트부터 지금까지 이어서 인쇄하거나

        dp = [0 for _ in range(self.n + 1)]
        checkpoint = 0

        for i in range(1, self.n + 1):
            if i in self.pages:
                dp[i] = dp[i-1]
            else:
                # 새로 체크포인트를 만들어 인쇄 시작
                option_1 = dp[i-1] + 7

                new_checkpoint = i

                # 이전 체크포인트부터 지금까지 이어서 인쇄
                if checkpoint != 0:
                    option_2 = dp[checkpoint] +  (i - checkpoint)*2
                else:
                    option_2 = 1e9

                if option_1 < option_2:
                    checkpoint = new_checkpoint
                    dp[i] = option_1

                else:
                    dp[i] = option_2

        print(dp[-1])

def main():
    instance = Problem()
    instance.run()

if __name__ == "__main__":
    main()