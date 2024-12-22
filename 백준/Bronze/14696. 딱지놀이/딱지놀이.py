import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a = list(map(int, input().split())) # A가 낸 딱지에 나온 그림의 총 개수, 딱지의 그림
    b = list(map(int, input().split())) # B가 낸 딱지에 나온 그림의 총 개수, 딱지의 그림

    # 4:별, 3:동그라미, 2:네모, 1:세모
    dic_a = defaultdict(int)
    dic_b = defaultdict(int)

    for i in range(1, a[0]+1):
        dic_a[a[i]] += 1
    for i in range(1, b[0]+1):
        dic_b[b[i]] += 1

    # 두 딱지의 별의 개수가 다르다면, 별이 많은 쪽의 딱지가 이긴다
    if dic_a[4] != dic_b[4]:
        if dic_a[4] > dic_b[4]:
            print("A")
        else:
            print("B")
    else:
        if dic_a[3] != dic_b[3]:
            if dic_a[3] > dic_b[3]:
                print("A")
            else:
                print("B")
        else:
            if dic_a[2] != dic_b[2]:
                if dic_a[2] > dic_b[2]:
                    print("A")
                else:
                    print("B")
            else:
                if dic_a[1] != dic_b[1]:
                    if dic_a[1] > dic_b[1]:
                        print("A")
                    else:
                        print("B")
                else:
                    print("D")