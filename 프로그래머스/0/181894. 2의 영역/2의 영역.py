def solution(arr):
    answer = []
    indices = []
    for i in range(len(arr)):
        if arr[i] == 2:
            indices.append(i)

    if len(indices) == 0:
        answer.append(-1)
    elif len(indices) == 1:
        answer.append(arr[indices[0]])
    else: 
        if indices[-1] == len(arr) - 1:
            answer = arr[indices[0]:]
        else:
            answer = arr[indices[0]:indices[-1] + 1]
        
    return answer