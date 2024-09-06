from itertools import combinations

def solution(relation):
    total_keys = [i for i in range(len(relation[0]))]
    combos = []
    for num in range(1, len(total_keys)+1):
        combos.extend(combinations(total_keys, num))
    
    stack = []
    for combo in combos:
        temp = set()
        for person in relation:
            temp.add(tuple([person[key] for key in combo]))
        if len(temp) == len(relation):
            is_break = 0
            for i in stack:
                if set(i).issubset(set(combo)):
                    is_break = 1
                    break
            if is_break == 0:
                stack.append(combo)
    answer = len(stack)
    return answer