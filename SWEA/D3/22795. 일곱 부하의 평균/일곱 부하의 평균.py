T = int(input())

for _ in range(T):
    arr = list(map(int, input().split()))
    answer = max(arr) + 1
    total = sum(arr)
    while True:
        if (total + answer)/7 == int((total + answer)/7):
            print(answer)
            break
        answer += 1