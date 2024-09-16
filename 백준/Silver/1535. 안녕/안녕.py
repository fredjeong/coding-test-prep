import sys

input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

hp = 100
joy = 0

def solution(N, L, J, hp, joy):
    arr = []
    def dfs(N, L, J, hp, joy, idx, visit):
        if visit == True:
            joy += J[idx]
            hp -= L[idx]
        
        if hp <= 0:
            return
        
        if idx == N-1:
            arr.append(joy)
            return
        
        dfs(N, L, J, hp, joy, idx+1, visit=True)
        dfs(N, L, J, hp, joy, idx+1, visit=False)

    dfs(N, L, J, hp, joy, 0, visit=True)
    dfs(N, L, J, hp, joy, 0, visit=False)
    return max(arr)

if __name__ == '__main__':
    result = solution(N, L, J, hp, joy)
    print(result)