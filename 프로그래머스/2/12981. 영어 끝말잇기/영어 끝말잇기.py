def solution(n, words):
    answer = [0, 0]
    for i in range(1, len(words)):
        current_word = words[i]
        previous_word = words[i-1]
        # 틀릴 조건 1: 전 단어의 마지막 글자와 현재 단어의 첫 번째 글자가 다를 시
        if current_word[0] != previous_word[-1]:
            num = i%n + 1
            lap = i//n + 1
            answer = [num, lap]
            break
        else:
            pass
        
        # 틀릴 조건 2: 이미 나온 단어를 얘기할 시
        if current_word in words[:i]:
            num = i%n + 1 # 탈락하는 사람의 번호
            lap = i//n + 1 # 자신의 몇 번째 차례에 탈락하는지
            answer = [num, lap]
            break
        else:
            pass
        
    return answer