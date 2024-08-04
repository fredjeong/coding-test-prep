def solution(array, n):
    positive_distance = []
    negative_distance = []
    for i in array:
        if n - i >= 0:
            positive_distance.append(n - i)
        else:
            negative_distance.append(n - i)
    if len(positive_distance) > 0:
        positive_min = min(positive_distance)
    else:
        positive_min = 500
    if len(negative_distance) > 0:
        negative_min = max(negative_distance)
    else:
        negative_min = 500
    if positive_min <= abs(negative_min):
        answer = n - positive_min
    else:
        answer = n - negative_min
    return answer