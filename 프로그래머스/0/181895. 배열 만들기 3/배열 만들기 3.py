def solution(arr, intervals):
    interval_1 = arr[intervals[0][0]:intervals[0][1]+1]
    interval_2 = arr[intervals[1][0]:intervals[1][1]+1]
    answer = interval_1 + interval_2
    return answer