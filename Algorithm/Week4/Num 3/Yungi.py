N, M = map(int, input().split(" "))
chicken_cnt = 0
chicken = []
house = []
city = [list(map(int, input().split(" "))) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])
            chicken_cnt += 1

chicken_check = [False for _ in range(chicken_cnt)]
min_sum = 999999
select_chicken_idx = [0 for _ in range(M)]


def f(k, n_chicken, house, chicken):
    global min_sum
    if k == M:
        inner_sum = 0
        for item in house:
            tmp_min_sum = 9999999
            for chick_idx in select_chicken_idx:
                tmp_min_sum = min(tmp_min_sum,
                                  abs(item[0] - chicken[chick_idx][0]) + abs(item[1] - chicken[chick_idx][1]))
            inner_sum += tmp_min_sum
        min_sum = min(inner_sum, min_sum)
        return

    for i in range(select_chicken_idx[k - 1], n_chicken):
        """
           어차피 우리는 combination을 찾아야하기에, 맨앞부터 체크하지말고, 이전에 체크햇던 idx 이후로만 체크 =>
           근데 사실 k-1이 0보다 작을 때를 고려해줘야하는데, 생각해보니 select_chicken_idx를 0으로 초기화 시켜줘서,
            k = 0일 때 그냥 select_chicken_idx[k-1]을 참조해와도 시작idx가 0이 나오기에 그냥 조건문 안씀
       """
        if not chicken_check[i]:
            select_chicken_idx[k] = i
            chicken_check[i] = True
            f(k + 1, n_chicken, house, chicken)
            chicken_check[i] = False


f(0, chicken_cnt, house, chicken)
print(min_sum)