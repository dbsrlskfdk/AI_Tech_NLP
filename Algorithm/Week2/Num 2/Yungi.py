N = int(input())
conf = []

for i in range(N):
    conf.append(list(map(int, input().split(" "))))

conf.sort(key=lambda x: x[0])
conf.sort(key=lambda x: x[1])

cnt = 0
end = 0
for i in range(N):
    if end > conf[i][0]:
        continue
    cnt += 1
    end = conf[i][1]
print(cnt)