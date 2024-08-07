def solution(sizes):
    widths = []
    heights = []
    for i in sizes:
        a, b = max(i), min(i)
        widths.append(a)
        heights.append(b)
    answer = max(widths) * max(heights)
    return answer