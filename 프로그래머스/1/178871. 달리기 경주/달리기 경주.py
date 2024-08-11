def solution(players, callings):
    rank = {player: i for i, player in enumerate(players)} # 선수, 등수 쌍으로 순위 딕셔너리 생성
    for name in callings:
        index = rank[name]
        rank[name] -= 1
        rank[players[index - 1]] += 1
        players[index - 1], players[index] = players[index], players[index - 1]
    return players