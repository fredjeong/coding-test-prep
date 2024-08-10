def solution(arr, queries):
    for query in queries:
        i = query[0]
        j = query[1]
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    return arr