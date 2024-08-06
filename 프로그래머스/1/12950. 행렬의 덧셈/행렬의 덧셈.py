def solution(arr1, arr2):
    rows = len(arr1)
    cols = len(arr1[0])
    answer = [[0 for j in range(cols)] for i in range(rows)]
    
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    
    return answer
