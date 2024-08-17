# Dynamic programming
def solution(n):
    # 기본 테이블을 모두 0으로 초기화하고 n=1, 2일 때의 값들만 미리 입력
    if n == 1:
        return 1
    else:
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        # 점화식 적용
        for i in range(3,n+1):
            dp[i] = (dp[i-2] + dp[i-1]) % 1234567
        return dp[-1]