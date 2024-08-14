def solution(brown, yellow):
    # (노란색의 가로 길이 + 노란색의 세로 길이 + 2) * 2 = brown
    # (h + w + 2) * 2 = brown
    # h * w = yellow
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            if (i + (yellow // i) + 2) * 2 == brown:
                answer = [yellow // i + 2, i + 2]
    return answer