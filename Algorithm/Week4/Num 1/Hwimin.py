N = int(input())    # N 입력받기
K = int(input())    # K 입력받기

board = [[0 for _ in range(N)] for _ in range(N)]   #NxN 크기의 board 만들기

for i in range(K):                      #board에 사과의 위치 입력
    x, y = map(int, input().split())
    board[x-1][y-1] = 2

L = int(input())     # L 입력받기
command_array = []
for i in range(L):    # 정수n과 문자command 입력받고 command_array에 리스트로 저장
    n, command = input().split()
    command_array.append((int(n), command))

snake = [(0, 0)]       #뱀의 머리와 몸의 좌표 리스트
D = {'D': (1, 0), 'U': (-1, 0), 'R': (0, 1), 'L': (0, -1)} #상하좌우'UDLR'의 좌표 변화값
direction = 'R'         #현재 뱀머리의 방향

answer = 0
while True:
    answer += 1 #시간 증가
    #뱀 머리의 현재위치 + 뱀 머리방향의 좌표 변화 값
    x, y = snake[-1][0]+D[direction][0], snake[-1][1]+D[direction][1]

    if x<0 or y<0 or x>=N or y>=N: #뱀 머리가 벽에 도달하는 경우
        break
    if board[x][y] == 1: #뱀의 머리가 이전의 몸과 부딪히는 경우
        break

    if command_array and answer == command_array[0][0]: #커맨드 리스트가 있고 시간조건이 동일하면
        if command_array[0][1] == 'D':  #우측회전 명령
            idx = 'URDL'.index(direction)
            direction = 'URDL'[idx+1] if idx < 3 else 'U'
        elif command_array[0][1] == 'L':   #좌측회전 명령
            idx = 'ULDR'.index(direction)
            direction = 'ULDR'[idx + 1] if idx < 3 else 'U'
        command_array.pop(0)    #커맨드 실행후 리스트에서 제거

    snake.append((x, y))    #이동한 머리위치 리스트에 저장
    if board[x][y] != 2:    #이동한 머리위치에 사과(=2)가 없으면 꼬리위치의 board 좌표제거
        x_tail, y_tail = snake.pop(0)
        board[x_tail][y_tail] = 0
    board[x][y] = 1     #머리 위치의 board 좌표 추가

print(answer)