def solution(arr, delete_list):
    answer = arr
    for i in delete_list:
        if i in answer:
            answer.remove(i)
    return answer