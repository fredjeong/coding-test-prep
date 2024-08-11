def solution(bandage, health, attacks):
    attack_dic = {}
    for i in range(len(attacks)):
        attack_dic[attacks[i][0]] = attacks[i][1]
    
    total_timesteps = attacks[-1][0]
    
    t = bandage[0]
    x = bandage[1]
    y = bandage[2]
    hp = health
    die = False
    current_timestep = 0
    cumulative_time = 0
    
    while current_timestep < attacks[-1][0]:
        current_timestep += 1
        if current_timestep in attack_dic: # 이번 턴에 공격을 받는 경우
            cumulative_time = 0 # 누적시간 초기화
            hp -= attack_dic[current_timestep] # 체력 감소
            # 체력이 0 이하가 되었다면 -1 리턴
            if hp <= 0:
                die = True # 사망
                break
        else: # 이번 턴에 공격을 받지 않은 경우
            hp = min(hp + x, health) # 체력 회복
            cumulative_time += 1 # 누적시간 1 추가
            if cumulative_time == t: # 보너스 체력
                hp = min(hp + y, health) # 최대 체력 초과할 수 없음
                cumulative_time = 0 # 누적시간 리셋
    if die:
        answer = -1
    else:
        answer = hp
    return answer