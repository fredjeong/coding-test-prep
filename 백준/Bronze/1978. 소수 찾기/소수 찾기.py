import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

def prime_list(num):
    visited = [False for _ in range(num+1)]
    visited[0] = True
    visited[1] = True
    for i in range(2, int(num**0.5+1)):
        if visited[i] == True:
            continue
        for j in range(2*i, num+1, i):
            if visited[j] == True:
                continue
            visited[j] = True

    return set(k for k in range(len(visited)) if visited[k] == False)

num = max(arr)
primes = prime_list(num)

count = 0
for i in arr:
    if i in primes:
        count += 1
print(count)