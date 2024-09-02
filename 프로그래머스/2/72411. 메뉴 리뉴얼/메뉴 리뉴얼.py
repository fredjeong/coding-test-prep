from itertools import combinations

def solution(orders, course):    
    answer = []

    for course_num in course:
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

    answer = sorted(answer)
    return answer