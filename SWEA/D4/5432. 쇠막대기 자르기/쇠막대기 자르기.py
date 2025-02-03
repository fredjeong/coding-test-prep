T = int(input()) # 테스트 케이스의 개수

for test_case in range(1, T+1):
    s = input().strip()
    total = 0
    stack = 0
    for i in range(len(s)):
        char = s[i]
        if char == "(":
            next_char = s[i+1]
            if next_char == "(": # 쇠막대기
                stack += 1
            
        else: 
            prev_char = s[i-1]
            if prev_char == "(": # 레이저
                total += stack
            else: # 쇠막대기 하나 끝
                stack -= 1
                total += 1
    total += stack
    print(f"#{test_case} {total}")