def solution(citations):
    citations = sorted(citations)
    h = 0
    cited = len(citations)
    if max(citations) == 0:
        return 0
    else:
        while h < cited:
            h += 1
            cited_temp = cited
            while citations[0] < h:
                citations.pop(0)
                cited -= 1
        return cited