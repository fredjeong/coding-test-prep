def solution(arr):
    arr_past = [] + arr
    answer = 0
    arr_new = [] + arr_past
    for i in range(len(arr_new)):
        if arr_new[i] >= 50 and arr_new[i] % 2 == 0:
            arr_new[i] = arr_new[i] // 2
        elif arr_new[i] < 50 and arr_new[i] % 2 == 1:
            arr_new[i] = arr_new[i] * 2 + 1
                
    while arr_past != arr_new:
        answer += 1
        arr_past = [] + arr_new
        for i in range(len(arr_new)):
            if arr_new[i] >= 50 and arr_new[i] % 2 == 0:
                arr_new[i] /= 2
            elif arr_new[i] < 50 and arr_new[i] % 2 == 1:
                arr_new[i] = arr_new[i] * 2 + 1

    return answer