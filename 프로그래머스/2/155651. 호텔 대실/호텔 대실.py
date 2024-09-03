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