def solution(progresses, speeds):
    stack = []
    while sum(stack) != len(progresses):
        count = 0
        for i in range(sum(stack), len(progresses)):
            progresses[i] += speeds[i]
        
        for i in range(sum(stack), len(progresses)):
            if progresses[i] >= 100:
                count += 1
            else:
                break
        if count != 0:
            stack.append(count)
    return stack
    