N, M, y, x, K = map(int, input().split(" "))
map_num = [list(map(int, input().split(" "))) for _ in range(N)]
movements = list(map(int, input().split(" ")))
dice = [[0, 0], [0, 0], [0, 0]] # [[아래, 위], [왼, 우], [앞, 뒤]]

def daegul(map_num, y, x, dice):
    if map_num[y][x] == 0:
        map_num[y][x] = dice[0][0]
    else:
        dice[0][0] = map_num[y][x]
        map_num[y][x] = 0
    print(dice[0][1])

for m in movements:
    if m == 1: # 동쪽 => 우측면 -> 아래면, 좌측면 -> 윗면, 아래면 -> 좌측면, 윗면 -> 우측면
        if x + 1 < M:
            dice[0][0], dice[0][1], dice[1][0], dice[1][1] = dice[1][1], dice[1][0], dice[0][0], dice[0][1]
            x += 1
            daegul(map_num, y, x, dice)
    elif m == 2: # 서쪽 => 좌측면 -> 아래면, 우측면 -> 윗면, 아래면 -> 우측면, 윗면 -> 좌측면
        if x - 1 >= 0:
            dice[0][0], dice[0][1], dice[1][0], dice[1][1] = dice[1][0], dice[1][1], dice[0][1], dice[0][0]
            x -= 1
            daegul(map_num, y, x, dice)
    elif m == 3: # 북쪽 => 아랫면 -> 뒷면, 윗면 -> 앞면, 앞면 -> 아랫면, 뒷면 -> 윗면
        if y - 1 >= 0:
            dice[0][0], dice[0][1], dice[2][0], dice[2][1] = dice[2][0], dice[2][1], dice[0][1], dice[0][0]
            y -= 1
            daegul(map_num, y, x, dice)
    elif m == 4: # 남쪽 => 아랫면 -> 앞면, 윗면 -> 뒷면, 앞면 -> 윗면, 뒷면 -> 아랫면
        if y + 1 < N:
            dice[0][0], dice[0][1], dice[2][0], dice[2][1] = dice[2][1], dice[2][0], dice[0][0], dice[0][1]
            y += 1
            daegul(map_num, y, x, dice)