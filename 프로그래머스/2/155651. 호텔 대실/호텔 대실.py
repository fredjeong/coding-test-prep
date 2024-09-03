import datetime

def solution(book_time):
    book_time = sorted(book_time, key=lambda x:x[0])
    stack = []
    for booking in book_time:

        entry = datetime.datetime.strptime(booking[0], '%H:%M').time()
        exit = datetime.datetime.strptime(booking[1], '%H:%M')
        ready = (exit + datetime.timedelta(minutes=10)).time()
        
        temp_1 = datetime.datetime.strptime('00:00', '%H:%M').time()
        temp_2 = datetime.datetime.strptime('00:09', '%H:%M').time()
        if ready >= temp_1 and ready <= temp_2:
            ready = datetime.datetime.strptime('23:59', '%H:%M').time()
        
        if len(stack) == 0:
            stack.append(ready)
            continue
        
        if entry >= min(stack):
            del stack[stack.index(min(stack))]
            stack.append(ready)
        else:
            stack.append(ready)

    answer = len(stack)
    return answer

# ["14:10", "19:20"] # stack = [19:30]
# ["14:20", "15:20"] # stack = [19:30, 15:30]
# ["15:00", "17:00"] # stack = [19:30, 15:30, 17:10]
# ["16:40", "18:20"] # stack = [19:30, 17:10, 18:30]
# ["18:20", "21:20"] # stack = [19:30, 18:30, 21:30]




 # 객실 준비시간만 넣으면 된다 단 10분 더했을때 자정이 넘어가면 안됨 
        # 입실시간이 준비시간 minimum보다 늦으면 교체
        # 입실시간이 준비시간 minimum보다 빠르면 추가

# ten_minutes_later = current + datetime.timedelta(minutes=10)

#    # 우선 입실시간 순으로 정렬한다
#    book_time = sorted(book_time, key=lambda x:x[0])
#    
#    # stack을 활용하자
#    stack = []
#    for booking in book_time:
#        # 객실을 하나 더 사용해야 하는 경우
#        
#        # 기존 객실에 집어넣을 수 있는 경우
#        if 
#        stack.append(book)
        
    