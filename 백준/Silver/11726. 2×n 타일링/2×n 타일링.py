import sys

input = sys.stdin.readline

n = int(input())

def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[-1]%10007

if __name__ == '__main__':
    result = solution(n)
    print(result)