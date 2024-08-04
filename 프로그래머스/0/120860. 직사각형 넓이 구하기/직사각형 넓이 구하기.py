def solution(dots):
    #print(dots[0][0] - dots[1][0])
    #print(distance(dots[0], dots[1]))
    length_list = []
    for i in range(1, 4):
        length_list.append(distance(dots[0], dots[i]))
    length_list = sorted(length_list)
    answer = length_list[0] * length_list[1]
    return answer
    
def distance(point_1, point_2):
    return ((point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2)**0.5