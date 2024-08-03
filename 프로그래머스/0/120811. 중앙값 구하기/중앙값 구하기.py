def solution(array):
    new_array = sorted(array)
    key = len(array) // 2
    answer = new_array[key]
    return answer