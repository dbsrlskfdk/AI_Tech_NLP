N, M = map(int, input().split())

temprow = []
homes = []
foods = []
for row in range(1, N+1):
    temprow = list(map(int, input().split()))
    for col, val in enumerate(temprow):
        if val == 1:
            homes.append( (row, col+1) )
        elif val == 2:
            foods.append( (row, col+1) )

import itertools
from collections import defaultdict
totsum_list = []
for newfoods in itertools.combinations(foods, M):
    dic = defaultdict(lambda : 1e10)
    for home, food in itertools.product(homes, newfoods):
        homer, homec = home[0], home[1]
        foodr, foodc = food[0], food[1]

        dist = abs(homer - foodr) + abs(homec - foodc)
        if dist < dic[home]:
            dic[home] = dist
    else :
        totsum = sum(dic.values())
        totsum_list.append(totsum)
else :
    totsum_list.sort()
    print(totsum_list[0])
#이렇게 하면 newfoods 내에 food1이 여러번 뽑힐 텐데, food1에 대한
#거리 계산이 전부 진행됨
#이중리스트 형식으로 food1에 대한 거리, food2에 대한 거리를 1번만 계산 후
#zip과 언팩 써서 home1과 food1, food2 에 대한 거리 중 min을
#combinations(foods, M)으로 하면 계산 간단화 가능
#t1