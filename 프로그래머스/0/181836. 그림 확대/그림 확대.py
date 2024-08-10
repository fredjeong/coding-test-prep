def solution(picture, k):
    original = [[picture[row][col] for col in range(len(picture[0]))] for row in range(len(picture))]
    new = [["A" for _ in range(len(picture[0] * k))] for _ in range(len(picture) * k)]
    for i in range(len(picture)):
        for j in range(len(picture[0])):
            for row in range(k):
                for col in range(k):
                    new[i*k+row][j*k + col] = original[i][j]
    answer = ['' for _ in range(len(picture)*k)]
    for i in range(len(new)):
        for j in range(len(new[0])):
            answer[i] += new[i][j]
    return answer