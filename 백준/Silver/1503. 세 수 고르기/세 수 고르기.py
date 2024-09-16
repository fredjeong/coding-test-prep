import sys

input = sys.stdin.readline

N, M = map(int, input().split())
S = set(map(int, input().split()))

arr = set([i for i in range(1, 1002)]) - S
answer = 1e9

for a in arr:
    for b in arr:
        for c in arr:
            answer = min(abs(N-a*b*c), answer)
            if a*b*c > N+1:
                break

print(answer)