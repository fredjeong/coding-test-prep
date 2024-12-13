import sys
input = sys.stdin.readline

n, k = map(int, input().split())

length_n = len(str(n))
length_seq = 0
for i in range(1, length_n):
    length_seq += 9 * 10**(i-1) * i

if length_n == 1:
    length_seq += n
else:
    length_seq += (n - int(str(9) * (length_n-1)))*length_n

if length_seq < k:
    print(-1)
else:
    k -= 1
    count = 0
    while True:
        if k <= 9 * 10**count * (count + 1):
            break
        k -= 9 * 10**count * (count + 1)
        count += 1

    num = 10**count + k//(count+1)
    answer = list(str(num))[k % (count+1)]
    print(answer)