def solution(fees, records):
    # fees = [기본 시간, 기본 요금, 단위 시간, 단위 요금]
    # 누적 주차 시간을 계산하여 요금 일괄 정산
    cum_time = {}
    in_times = {}
    for record in records:
        record = record.split(" ")
        if record[2] == "IN":
            in_times[record[1]] = record[0]
        if record[2] == "OUT":
            in_time = in_times[record[1]] # 입차 시간 불러오기
            out_time = record[0]
            
            hour = int(out_time[:2]) - int(in_time[:2])
            minutes = int(out_time[3:]) - int(in_time[3:])
            
            if record[1] in cum_time:
                cum_time[record[1]] += hour * 60 + minutes
            else:
                cum_time[record[1]] = hour * 60 + minutes
            
            del in_times[record[1]] # 지워주기
        
        
    # 다 끝나고도 남아있는 차가 있다면 출차 23:59 적용
    for i in in_times:
        hour = 23 - int(in_times[i][:2])
        minutes = 59 - int(in_times[i][3:])
        if i in cum_time:
            cum_time[i] += hour * 60 + minutes
        else:
            cum_time[i] = hour * 60 + minutes
            
    # 요금 계산
    answer = []
    arr = sorted(cum_time.items())
    
    for i in arr:
        if i[1] < fees[0]:
            answer.append(fees[1])
        else:
            base = fees[1]
            if (i[1] - fees[0]) % fees[2] == 0:
                add = ((i[1] - fees[0]) // fees[2]) * fees[3]
            else:
                add = (((i[1] - fees[0]) // fees[2]) + 1) * fees[3]
            total = base + add
            answer.append(total)
            
    
    return answer