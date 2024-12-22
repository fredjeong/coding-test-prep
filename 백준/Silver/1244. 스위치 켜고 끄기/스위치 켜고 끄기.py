import sys

input = sys.stdin.readline

n = int(input())
switch = list(map(int, input().split()))

n_students = int(input())
for _ in range(n_students):
    sex, num = map(int, input().split())
    num -= 1
    if sex == 1:
        for i in range(num, n, num+1):
            if switch[i] == 0:
                switch[i] = 1
            else:
                switch[i] = 0
    else:
        if switch[num] == 0:
            switch[num] = 1
        else:
            switch[num] = 0

        dis = 1
        while num - dis >= 0 and num + dis < n:
            if switch[num-dis] != switch[num+dis]:
                break

            if switch[num-dis] == 0:
                switch[num-dis] = 1
                switch[num+dis] = 1
            else:
                switch[num-dis] = 0
                switch[num+dis] = 0

            dis += 1

for row in range(n // 20):
    print(" ".join(map(str, switch[row*20:row*20+20])))

print(" ".join(map(str, switch[n//20 * 20:])))