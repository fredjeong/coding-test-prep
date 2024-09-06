import datetime

def solution(plans):
    answer = []
    stack = []
    
    # 우선 과제를 시작 시각 순으로 정렬
    plans = sorted(plans, key=lambda x:x[1])
    #print(plans)
    # 과제 시작
    for i in range(len(plans)):
        if i == len(plans) - 1:
            answer.append(plans[i][0])
            continue
        
        name = plans[i][0]
        start = plans[i][1]
        period = plans[i][2]
        start = datetime.datetime.strptime(start, '%H:%M')
        period = datetime.timedelta(minutes=int(period))
        end = (start + period)
        next_start = datetime.datetime.strptime(plans[i+1][1], '%H:%M')
        
        if end > next_start: # 과제를 중간에 멈춰야 하는 경우
            stop = True
            timediff = int((end - next_start).seconds / 60)
        else:
            stop = False
            timediff = int((next_start - end).seconds / 60)

        if stop == True:
            stack.append([name, timediff])
        else:
            answer.append(name)
            if stack:
                while timediff > 0:
                    temp_name, temp_timeleft = stack.pop()
                    new_temp_timeleft = temp_timeleft - timediff
                    if new_temp_timeleft <= 0: # timediff >= new_temp_timeleft
                        answer.append(temp_name)
                        timediff -= temp_timeleft
                    else:
                        stack.append([temp_name, new_temp_timeleft])
                        timediff -= temp_timeleft
                    
                    if len(stack) == 0:
                        break
        
    for _ in range(len(stack)):
        answer.append(stack.pop()[0])
    
    
    return answer