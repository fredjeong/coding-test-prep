import sys

input = sys.stdin.readline

a, b = input().strip().split()

len_a = len(a)
len_b = len(b)
if len_a == len_b:
    count = 0
    for i in range(len_a):
        if a[i]!=b[i]:
            count += 1
    print(count)

else:
    minimum = 1e9
    start = 0
    end = len_a
    while end <= len_b:
        if end==len_b:
            temp = b[start:]
        else:
            temp = b[start:end]
        count = 0
        for i in range(len_a):
            if a[i]!=temp[i]:
                count += 1
        minimum = min(minimum, count)
        start += 1
        end += 1
    print(minimum)