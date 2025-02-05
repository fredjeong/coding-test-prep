T = int(input())

# 숫자는 고정시키고 연산자의 위치를 변경시켜야 함
def dfs(result, idx, visited):
    if len(result) == n-1:
        results.append(result)
        return

    for next_idx in range(4):
        visited_ = visited[:]
        if visited_[next_idx] == 0:
            continue
        visited_[next_idx] -= 1
        dfs(result + [next_idx], next_idx, visited_)

dic = {0: "+", 1: "-", 2: "*", 3: "/"}

for test_case in range(1, T+1):
    n = int(input())
    operators_dic = {}
    operators = list(map(int, input().split())) # 순서대로 +, -, *, /

    nums = list(map(int, input().split()))

    max_val = -1e9
    min_val = 1e9
    
    for i in range(4):
        # visited의 각 인덱스 값은 해당 연산자의 남은 사용 가능 횟수
        visited = operators[:]

        if not visited[i]:
            continue
        visited[i] -= 1

        results = []
        dfs([i], i, visited) # 각 연산자에 대하여 탐색

        for case in results:
            case_interpreted = [dic[num] for num in case]

            val = nums[0]

            for i in range(n-1):
                if case_interpreted[i] == "+":
                    val += nums[i+1]
                elif case_interpreted[i] == "-":
                    val -= nums[i+1]
                elif case_interpreted[i] == "*":
                    val *= nums[i+1]
                elif case_interpreted[i] == "/":
                    val = int(val / nums[i+1])

            max_val = max(max_val, val)
            min_val = min(min_val, val)

    print(f"#{test_case} {max_val - min_val}")