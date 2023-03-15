num = int(input())
infos = []
for i in range(num):
    temp = list(map(int, input().split(' ')))
    infos.append(temp)

infos.sort(key=lambda x: (x[1], x[0]))
prev_end = 0
cnt = 0
for start, end in infos:
    if start >= prev_end:
        prev_end = end
        cnt += 1
print(cnt)