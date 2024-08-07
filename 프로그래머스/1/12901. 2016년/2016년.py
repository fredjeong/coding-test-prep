def solution(a, b):
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    arr = [[1, 31], [2, 29], [3, 31], [4, 30], [5, 31], [6, 30], 
           [7, 31], [8, 31], [9, 30], [10, 31], [11, 30], [12, 31]]
    if a != 1:
        total_days = 0
        for i in range(a-1):
            total_days += arr[i][1]
        total_days += b - 1
    else:
        total_days = b - 1
    answer = day[total_days % 7]
    return answer