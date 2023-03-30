#https://kim519620.tistory.com
#강하게 영향을 받은 2차 출처
def solution(key, lock):
    def turn(arr):
        alen = len(arr)
        new = [['a' for x in range(alen)] for xx in range(alen)]
        for i in range(alen):
            for j in range(alen):
                new[j][alen-1-i] = arr[i][j]
        return new
    # def turn(arr):
    #     return list(map(list, zip(*arr[::-1])))
    # 741, 852, 963
    def check(arr, N):
        answer = True
        for ix in range(N):
            for iy in range(N):
                if arr[ix + N][iy + N] != 1:
                    return False
        return answer

    
    
    # 3배 더 큰 자물쇠 생성
    M = len(key)
    N = len(lock)
    new_lock = [[2] * N * 3 for _ in range(N * 3)]
    for ix in range(N):
        for iy in range(N):
            new_lock[ix + N][iy + N] = lock[ix][iy]
    original = [single[:] for single in new_lock]
    
    # 시계방향으로 4번 돌림
    for _ in range(4):
        key = turn(key)
        for lock_ix in range(N * 2):
            for lock_iy in range(N * 2):
                # key를 new_lock에 꽂음
                for key_ix in range(M):
                    for key_iy in range(M):
                        new_lock[lock_ix + key_ix][lock_iy + key_iy] += key[key_ix][key_iy]
                # new_lock의 중앙만 확인
                if check(new_lock, N):
                    return True
                # key를 new_lock에서 뺌
                new_lock = [single[:] for single in original]
                # for key_ix in range(M):
                #     for key_iy in range(M):
                #         new_lock[lock_ix + key_ix][lock_iy + key_iy] -= key[key_ix][key_iy]
    else :
        return False