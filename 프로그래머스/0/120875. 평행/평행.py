def solution(dots):
    def slope(p1, p2):
        return (p2[1] - p1[1]) / (p2[0] - p1[0])

    pairs = [
        (0, 1, 2, 3),
        (0, 2, 1, 3),
        (0, 3, 1, 2)
    ]
    
    for p1, p2, p3, p4 in pairs:
        if slope(dots[p1], dots[p2]) == slope(dots[p3], dots[p4]):
            return 1
    
    return 0