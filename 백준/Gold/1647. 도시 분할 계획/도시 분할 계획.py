import sys
input = sys.stdin.readline

# 자기랑 연결되어있는 최상위 부모노드를 찾는 함수
def find(n):
    # 부모가 자기 자신이 아니면 다시 탐색
    if parent[n] != n:                  
        parent[n] = find(parent[n])     
    return parent[n]                    

# 두개를 합칠때 더 작은 애를 부모노드로 적어서 합치기
def union(a, b):
    a = find(a)         
    b = find(b)         
    if a < b:           
        parent[b] = a   
    else:               
        parent[a] = b  


n,m = map(int,input().split())

edges = []
parent = [i for i in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append((a,b,c))

# 유지비의 합이 최소값이 되야하니까 유지보수값이 작은 순으로 나열하면서 먼저 확인
edges.sort(key=lambda x: x[2])

ans= 0
last_edge = 0
for a, b, c in edges:
    # 만약 두대가 연결되어있지 않으면 합치고 유지비 더하기
    if find(a) != find(b):
        union(a, b)
        ans += c
        last_edge = c
print(ans - last_edge)