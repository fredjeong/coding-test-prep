def solution(my_string, queries):
    answer = ''
    for query in queries:
        s = query[0]
        e = query[1]
        if s == e:
            pass
        else:
            if s == 0 and e == len(my_string) - 1:
                temp = ''
                for i in range(s, e+1):
                    temp = my_string[i] + temp
                my_string = temp
            elif s == 0 and e != len(my_string) - 1:
                temp = ''
                for i in range(s, e+1):
                    temp = my_string[i] + temp
                my_string = temp + my_string[e+1:]
            elif s != 0 and e == len(my_string) - 1:
                temp = ''
                for i in range(s, e+1):
                    temp = my_string[i] + temp
                my_string = my_string[:s] + temp
            else:
                temp = ''
                for i in range(s, e+1):
                    temp = my_string[i] + temp
                my_string = my_string[:s] + temp + my_string[e+1:]
    answer = my_string
    return answer