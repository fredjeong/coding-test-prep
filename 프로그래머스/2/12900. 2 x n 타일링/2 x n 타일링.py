# 피보나치 수열
def solution(n):
    dp = [0 for i in range(n)]
    dp[0], dp[1] = 1, 2
    for i in range(2, n):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    return dp[n-1]

## 예시는 통과했으나 런타임 에러 발생
#def solution(n):
#    global answer
#    answer = 0
#    def dfs(leftover): 
#        global answer
#        if leftover < 0:
#            return
#        elif leftover == 0:
#            answer += 1
#            return
#        elif leftover > 0:
#            temp_1 = leftover - 1
#            temp_2 = leftover - 2
#            dfs(temp_1)
#            dfs(temp_2)
#    
#    dfs(n)
#    answer %= 1000000007
#
#    return answer