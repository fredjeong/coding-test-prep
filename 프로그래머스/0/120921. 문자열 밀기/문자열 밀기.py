def solution(A, B):
    if A == B:
        answer = 0
    else:
        answer = 0
        new = A
        for i in range(1, len(A)+1):
            new = new[-1] + new[0:-1]
            if new == B:
                answer = i
                break
        if answer == 0:
            answer = -1
    return answer