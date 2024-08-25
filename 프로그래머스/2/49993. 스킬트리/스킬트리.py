def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        mastered = [False for _ in range(len(skill))]
        for char in tree:
            if char in skill:
                index = skill.index(char) 
                if index == 0:
                    mastered[index] = True
                else:
                    if mastered[index - 1] == False:
                        break
                    else:
                        mastered[index] = True
            
            if char == tree[-1]:
                answer += 1
                
    return answer