def solution(absolutes, signs):
    arr = []
    for i, j in zip(absolutes, signs):
        if j == True:
            arr.append(int(i))
        else:
            arr.append(-int(i))
    answer = sum(arr)
    return answer