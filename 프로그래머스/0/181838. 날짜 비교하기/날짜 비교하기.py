def solution(date1, date2):
    year = [date1[0], date2[0]]
    month = [date1[1], date2[1]]
    day = [date1[2], date2[2]]
    if year[0] <= year[1]:
        if year[0] < year[1]:
            answer = 1
        else:
            if month[0] <= month[1]:
                if month[0] < month[1]:
                    answer = 1
                else:
                    if day[0] < day[1]:
                        answer = 1
                    else:
                        answer = 0
            else:
                answer = 0
    else:
        answer = 0
    return answer