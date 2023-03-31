from collections import deque
body = deque()
head=[1, 1]
direction = 2
# left up right down
# 0    1   2     3
dic = {
    0:[0, -1],
    1:[-1, 0],
    2:[0, 1],
    3:[1, 0]
}

N = int(input())

K = int(input())
apples = []
for _ in range(K):
    apple=list(map(int,input().split()))
    apples.append(apple)

L = int(input())
infos = deque()
for _ in range(L):
    info = input().split()
    info[0] = int(info[0])
    infos.append(info)

second = 0
while True:
    second += 1
    temprow = head[0]+dic[direction][0]
    tempcol = head[1]+dic[direction][1]
    if temprow==0 or temprow>N:
        break
    if tempcol==0 or tempcol>N:
        break
    temphead = [temprow, tempcol]
    if temphead in body:
        break
    body.append(head)
    head = temphead

    if head in apples:
        apples.remove(head)
    else :
        body.popleft()

    if infos and infos[0][0] == second:
        _, order = infos.popleft()
        if order == 'D':
            direction += 1
            if direction == 4:
                direction = 0
        elif order == 'L':
            direction -= 1
            if direction == -1:
                direction = 3
    # print('body', body, 'head', head, second, direction)

######
print(second)
#t2