import sys

input = sys.stdin.readline

n = int(input())

a, b = map(int, input().split())

if n==1:
    print(1, min(a,b))
else:
    dic = {}
    dic[a] = 1
    dic[b] = 1
    
    dp = [[] for _ in range(n)]
    dp[0] = [1, min(a,b)]

    for i in range(1, n):
        a, b = map(int, input().split())
        
        keys = list(dic.keys())
        for key in keys:
            if key != a and key != b:
                del dic[key]

        if a==b:
            if a in dic:
                dic[a] += 1
            else:
                dic[a] = 1
        else:
            if a in dic:
                dic[a] += 1
            else:
                dic[a] = 1
            if b in dic:
                dic[b] += 1
            else:
                dic[b] = 1
        
        temp = sorted(dic.items(), key=lambda x:[-x[1], x[0]])
        dp[i] = [temp[0][1], temp[0][0]]
    
    result = sorted(dp, key=lambda x:[-x[0], x[1]])
    print(result[0][0], result[0][1])