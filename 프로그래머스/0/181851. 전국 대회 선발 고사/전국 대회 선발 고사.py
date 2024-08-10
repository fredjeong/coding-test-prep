def solution(rank, attendance):
    attended = []
    for i in range(len(rank)):
        if attendance[i] == True:
            attended.append([i, rank[i]])
    attended = sorted(attended, key = lambda x : x[1])
    a = attended[0][0]
    b = attended[1][0]
    c = attended[2][0]
    answer = 10000 * a + 100 * b + c
    return answer