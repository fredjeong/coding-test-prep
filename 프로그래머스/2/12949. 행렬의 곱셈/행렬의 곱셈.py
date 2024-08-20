def solution(arr1, arr2): 
    # 행렬의 곱셈은 arr1의 행의 각 성분 X arr2 열의 각 성분
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer