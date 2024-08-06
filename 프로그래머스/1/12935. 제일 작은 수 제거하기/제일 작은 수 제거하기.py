def solution(arr):
    answer = arr
    if len(arr) == 1:
        answer = [-1]
    else:
        answer.remove(min(arr))
    return answer