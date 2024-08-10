def solution(arr):
    answer = []
    length = len(arr)
    count = 0
    while length != 1:
        length /= 2
        if length == 1:
            break
        else:
            if length != int(length): 
                count += 1
                length = len(arr) + count
    for _ in range(count):
        arr.append(0)
    return arr