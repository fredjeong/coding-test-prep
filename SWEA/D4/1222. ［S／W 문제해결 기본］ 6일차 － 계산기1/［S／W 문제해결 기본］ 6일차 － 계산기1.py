from collections import deque

for test_case in range(1, 11):
    length = int(input())
    s = input().strip()
    
    stack = ""

    add_operator = False
    # 후위 표기식으로 바꾸기
    for char in s:
        if char.isdigit():
            stack += char
            if add_operator:
                stack += "+"
                add_operator = False
        else:
            add_operator = True
    
    # 계산
    arr = deque()
    for char in stack:
        if char.isdigit():
            arr.append(int(char))
        else:
            num_1 = arr.pop()
            num_2 = arr.pop()
            arr.appendleft(num_1 + num_2)
    print(f"#{test_case} {arr[0]}")