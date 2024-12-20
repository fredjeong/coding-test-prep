import sys
from collections import defaultdict

input = sys.stdin.readline

n, k = map(int, input().split())

dic = defaultdict(int)

for _ in range(n):
    # s는 0 또는 1, y는 학년
    s, y = map(int, input().split())

    # 성별과 학년을 붙여서 딕셔너리 키로 저장하는 방법은?
    key = str(s) + str(y)
    dic[key] += 1

count = 0
for key in dic.keys():
    if dic[key]%k == 0:
        count += dic[key]//k
    else:
        count += dic[key]//k + 1

print(count)