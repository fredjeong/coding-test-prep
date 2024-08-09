def solution(arr, idx):
    answer = -1
    for i in range(len(arr)):
        if i >= idx:
            if arr[i] == 1:
                answer = i
                break
    return answer