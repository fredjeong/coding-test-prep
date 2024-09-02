from itertools import combinations

def solution(orders, course):
    course_num_arr = []
    for order in orders:
        if len(order) not in course_num_arr:
            course_num_arr.append(len(order))
    
    answer = []
    max_num_dishes = 0
    for order in orders:
        if len(order) > max_num_dishes:
            max_num_dishes = len(order)
    course_num = 2
    for course_num in course:
    #while course_num <= max_num_dishes:
        course = {}
        for order in orders:
            comb = list(combinations(sorted(order), course_num))
            for choice in comb:
                choice = "".join(choice)
                if choice in course:
                    course[choice] += 1
                else:
                    course[choice] = 1
        for i in course:
            if course[i] == max(course.values()) and max(course.values()) > 1:
                answer.append(i)
        #course_num += 1

    answer = sorted(answer)
    return answer