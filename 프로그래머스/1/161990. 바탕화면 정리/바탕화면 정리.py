def solution(wallpaper):
    # 그냥 모든 좌표 중에서 제일 가까운 것, 제일 먼 것을 모으면 된다!
    x_coordinates = []
    y_coordinates = []
    
    for row in range(len(wallpaper)):
        for col in range(len(wallpaper[0])):
            if wallpaper[row][col] == "#":
                x_coordinates.append(row)
                y_coordinates.append(col)
    
    lux = min(x_coordinates)
    luy = min(y_coordinates)
    rdx = max(x_coordinates) + 1
    rdy = max(y_coordinates) + 1
    
    answer = [lux, luy, rdx, rdy]
    return answer
    
    
#    # 드래그를 하면 파일들을 선택할 수 있고, 선택한 파일들을 삭제할 수 있다.
#    # 최소한의 이동거리를 갖는 한 번의 드래그로 모든 파일을 선택해서 한 번에 지우려 한다.
#    # lux < rdx, luy < rdy 조건
#    # distance = abs(rdx - lux) + abs(rdy - luy)
#    # 좌표 선택 시엔 range 끝점 len() + 1 해야 함 
#    
#    # 0,0에 가장 가까운 # 위치 파악
#    distances = {}
#    for row in range(len(wallpaper)):
#        for col in range(len(wallpaper[0])):
#            if wallpaper[row][col] == "#":
#                distance = row + col
#                distances[distance] = [row, col]
#    
#    start_coordinate = sorted(distances.items(), key = lambda x: x[0])[0][1]
#        
#    # 가장 가까운 점 기준 이전 행, 이전 열에 파일 있는지 확인
#    # 0,0에 가장 가까운 행과 열을 찾았다!
#    # 첫 번째 행부터 가장 가까운 행까지 내려오면서 #를 포함하는 행이 발견됐다면 시작하는 행을 위로 땡겨야 한다.
#    for row in range(start_coordinate[0]):
#        if "#" in wallpaper[row]:
#            start_coordinate[0] = row 
#            break
#    # 첫 번째 열부터 가장 가까운 열까지 오른쪽으로 옮기면서 #를 포함하는 열이 발견됐다면 시작하는 열을 왼쪽으로 땡겨야 한다.
#    for col in range(start_coordinate[1]):
#        for i in range(len(wallpaper)):
#            if wallpaper[i][col] == "#":
#                start_coordinate[1] = col
#                break
#    
#    # 여기까지 하면 start 좌표가 잡힌다.
#    lux = start_coordinate[1]
#    luy = start_coordinate[0]
#    
#    # 같은 방법으로 5,5에 가장 가까운 #의 위치를 파악한다.
#    # 또는, 0,0에서 가장 멀리 떨어진 애를 찾으면 되지 않을까?
#    for row in range(len(wallpaper)):
#        for col in range(len(wallpaper[0])):
#            if wallpaper[len(wallpaper) - 1 - row][len(wallpaper[0]) - 1 - col] == "#":
#                end_coordinate = [row, col]
#                break
#    
#    end_coordinate = sorted(distances.items(), key = lambda x: x[0])[-1][1]
#    
#    # 행의 총 개수가 5이고, 가장 가까운 점의 행 인덱스가 2였다고 하자. 그러면 3이랑 4를 봐야하는데, 4부터 시작해서 3까지 와야 한다.
#    if end_coordinate[0] != len(wallpaper) - 1:
#        for row in range(len(wallpaper) - end_coordinate[0]):
#            if "#" in wallpaper[len(wallpaper) - 1 - row]:
#                end_coordinate[0] = row 
#                break
#    
#    if end_coordinate[1] != len(wallpaper[0]) - 1:
#        for col in range(len(wallpaper[0]) - end_coordinate[1]):
#            for i in range(len(wallpaper)):
#                if wallpaper[i][len(wallpaper[0]) - 1 - col] == "#":
#                    end_coordinate[1] = col
#                    break
#    # end 좌표 설정
#    rdx = end_coordinate[1] + 1
#    rdy = end_coordinate[0] + 1
#        
#        
#    # 5,5에 가장 가까운 # 위치 파악
#    # 가장 가까운 점 기준 뒤 행, 뒤 열에 파일 있는지 확인
#        # 있다면 드래그 끝점을 그 곳으로 잡고 rdx, rdy 선언
#        
#        # 없다면 가장 가까운 점을 끝점으로 잡고 rdx, rdy 선언
#        
#    
#
#    answer = [lux, luy, rdx, rdy]
#    return answer
#    #print(end_coordinate)