def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    
    prev_cam = -1e9
    cnt = 0
    for start, end in routes:
        if prev_cam < start:
            cnt += 1
            prev_cam = end
    return cnt