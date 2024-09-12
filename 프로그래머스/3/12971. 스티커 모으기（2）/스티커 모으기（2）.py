def solution(sticker):
    length = len(sticker)
    if length == 1:
        return sticker[0]
    if length == 2:
        return max(sticker[0], sticker[1])
    
    # 첫 번째를 뽑는 경우
    dp1 = [0 for _ in range(length-1)]
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    idx = 2
    for i in range(2, len(dp1)):
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
    # 첫 번째를 뽑지 않는 경우    
    dp2 = [0 for _ in range(length)]
    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2, len(dp2)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
    
    return max(dp1[-1], dp2[-1])