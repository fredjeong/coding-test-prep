import sys

input = sys.stdin.readline

N = int(input())

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    
    if n>1:
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = (dp[i-1] + dp[i-2])%1000000000
        return dp[-1]
    elif n<0:
        dp = [0 for _ in range(-n+1)]
        dp[1] = 1
        for i in range(2, -n+1):
            if i%2==0:
                dp[i] = -((dp[i-1]-dp[i-2]) % 1000000000)
            else:
                dp[i] = (dp[i-2] - dp[i-1]) % 1000000000
        return (dp[-1])

if __name__=="__main__":
    result = fib(N)
    if result>0:
        print(1)
    elif result==0:
        print(0)
    else:
        print(-1)
    print(abs(result))