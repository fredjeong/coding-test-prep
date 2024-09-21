import sys

input = sys.stdin.readline

N = int(input())

dic = {}
q = []
total = 0

for _ in range(N):
    num = int(input())
    q.append(num)
    total += num
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1


# 산술평균
print(round(total/N))

# 중앙값
q.sort()
print(q[N//2])

# 최빈값
arr = sorted(dic.items(), key=lambda x: [-x[1], x[0]])
if len(arr) == 1:
    print(arr[0][0])
else:
    if arr[0][1] == arr[1][1]:
        print(arr[1][0])
    else:
        print(arr[0][0])

# 범위
print(q[-1] - q[0])