def solution(arr):
    answer = 0
    arr_past = arr
    while True:
        arr_new = []
        for i in arr_past:
            if i >= 50 and i % 2 == 0:
                i = i // 2
            elif i < 50 and i % 2 == 1:
                i = i * 2 + 1
            arr_new.append(i)
        if arr_new == arr_past:
            break
        else:
            arr_past = arr_new
            answer += 1
    return answer