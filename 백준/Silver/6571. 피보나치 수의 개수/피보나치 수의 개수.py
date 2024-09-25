import sys

input = sys.stdin.readline

while True:
    a, b = map(int, input().split())
    if a==0 and b==0:
        break
    if a > b:
        print(0)
        continue
    result = 0
    dp = [1, 2]
    for i in dp:
        if a<=i<=b:
            result += 1
    
    if b <= 2:
        print(result)
        continue
    
    while True:
        num = dp[-1] + dp[-2]
        if num > b:
            break
        if a<=num<=b:
            result += 1
        dp.append(num)

    print(result)