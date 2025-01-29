from collections import deque

for test_case in range(1, 11):
    n = int(input())
    encrypted_arr = list(map(int, input().split()))
    m = int(input())
    order_arr = deque(input().split())
    index = 0
    while order_arr:
        order = order_arr.popleft()

        # 명령어가 I인 경우
        if order == "I":
            x = int(order_arr.popleft())
            y = int(order_arr.popleft())
            for index in range(x, x+y):
                temp = int(order_arr.popleft())
                encrypted_arr.insert(index, temp)

        # 명령어가 D인 경우
        elif order == "D":
            x = int(order_arr.popleft())
            y = int(order_arr.popleft())
            del encrypted_arr[x+1:x+y+1]

        # 명령어가 A인 경우
        elif order == "A":
            y = int(order_arr.popleft())
            for _ in range(y):
                temp = int(order_arr.popleft())
                encrypted_arr.append(temp)

    answer = " ".join(map(str, encrypted_arr[:10]))
    print(f"#{test_case} {answer}")