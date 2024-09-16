import sys
from collections import deque

input = sys.stdin.readline

string = str(input().strip())

def solution(string):
    nums = deque()
    opers = deque()
    formula = ""
    stack = ""
    for i in range(len(string)):
        if i == len(string)-1:
            stack += string[i]
            formula += str(int(stack))
            nums.append(int(stack))
        if string[i].isdigit():
            stack += string[i]
        else:
            formula += str(int(stack)) + string[i]
            nums.append(int(stack))
            stack = ""
            opers.append(string[i])

    if len(nums) == 1:
        return nums[0]
    
    elif len(nums) == 2:
        answer = nums.popleft()
        while opers:
            oper = opers.popleft()
            num = nums.popleft()
            if oper == "+":
                answer += num
            else:
                answer -= num
        return answer

    else:
        answer = nums.popleft()
        
        idx = 0
        while idx < len(opers):
            if opers[idx] == "+":
                answer += nums[idx]
                idx += 1
            else:
                if idx == len(opers)-1:
                    answer -= nums[idx]
                    idx += 1
                    continue
                stack = nums[idx]
                idx += 1
                while idx < len(opers):
                    if opers[idx] == "+":
                        stack += nums[idx]
                        if idx == len(opers)-1:
                            answer -= stack
                        idx += 1

                    else:
                        answer -= stack
                        break
        return answer

if __name__ == '__main__':
    result = solution(string)
    print(result)