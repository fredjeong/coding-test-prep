def solution(a, b):
    ab = int(str(a) + str(b))
    alt = 2 * a * b
    if ab >= alt:
        answer = ab
    else:
        answer = alt
    return answer