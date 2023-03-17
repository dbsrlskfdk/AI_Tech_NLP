def solution(routes):
    answer = 0
    roads = sorted(routes, key=lambda x : x[0])
    roads = sorted(roads, key=lambda x : x[1])
    past_end_point = -999999 # 최소 진입 지점이 -30000이라 더 작은 수로
    for road in roads:
        if past_end_point < road[0]:
            answer += 1
            past_end_point = road[1]

    return answer