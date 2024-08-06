def solution(arr):
    answer = [arr[0]]
    for i in range(1,len(arr)+1):
        if arr[i-1] != answer[-1]:
            answer.append(arr[i-1])
    return answer