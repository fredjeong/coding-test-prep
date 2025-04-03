#14889 스타트와 링크
#최대 n은 갯수는 20이고, 그중 절반을 뽑는 조합을 만들어서 계산하면 되지않을까
#n//2명을 뽑는 조합, 이렇게 뽑은 조합으로 각각의 팀 합을 구해서 => 포문을 돌면서 해당 팀배열에 수가 있으면 돌기..
n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]
def check(tlst):
    #tlst와 상대팀의 선수 배열 
    other = []
    tlst.sort()
    other.sort()
    for i in range(1,n+1):
        if i not in tlst:
            other.append(i)
    tlst_sum = 0
    #2중포문으로 돌면서 값 더하기 일단 행 
    for i in tlst:
        for j in tlst:
            tlst_sum += graph[i-1][j-1]
    
    other_sum = 0
    for i in other:
        for j in other:
            other_sum += graph[i-1][j-1]
    
    return abs(tlst_sum - other_sum)

    
mn = 1000000
#선수들의 번호는 1번부터 n번까지 ~ 
def dfs(num,tlst,s):
    global mn
    if num == n//2:
        mn = min(mn,check(tlst))
        return
    for i in range(s,n+1):
        dfs(num+1,tlst+[i],i+1)

dfs(0,[],1)
print(mn)
