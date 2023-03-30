from itertools import combinations
N, M = map(int, input().split())

house = []
chicken = []

for i in range(N):
    arr = list(map(int, input().split()))
    for idx, n in enumerate(arr):
        if n == 1:
            house.append((i, idx))
        elif n == 2:
            chicken.append((i, idx))

dist = [[abs(chicken[c][0]-house[h][0])+abs(chicken[c][1]-house[h][1]) for h in range(len(house))] for c in range(len(chicken))]
# dist=[]
# for c in range(len(chicken)):
#     tmp=[]
#     for h in range(len(house)):
#         tmp.append( abs(chicken[c][0]-house[h][0]) + abs(chicken[c][1]-house[h][1]) )
#     dist.append(tmp)

#예제 1번기준
#house = [(0, 2), (1, 4), (2, 1), (3, 2)]
#chicken = [(1, 2), (2, 2), (4, 4)]
#dist = [[1, 2, 2, 2], [2, 3, 1, 1], [6, 3, 5, 3]]


answer=[]
for combi in combinations(dist, M):
    tmp=[]
    for d in zip(*combi):   #combi = ([1, 2, 2, 2], [2, 3, 1, 1]), zip(*combi) = ((1,2), (2,3), (2,1), (2,1))
        tmp.append(min(d))
    answer.append(sum(tmp))
# answer = [sum([min(d) for d in zip(*combi)]) for combi in combinations(dist, M)]

#예제 3번 기준
#answer = [15, 12, 11, 12, 15]
print(min(answer))
