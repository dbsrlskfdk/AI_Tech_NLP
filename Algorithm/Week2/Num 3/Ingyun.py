input_ = list(input())

cnt_0 = 0
cnt_1 = 0
prev = ''
for i in input_:
    if i == prev:
        pass
    else :
        prev = i
        #리스트 혹은 딕트 타입으로
        #범용적으로 쓰는 게 나을 듯
        if i == '0':
            cnt_0 += 1
        elif i == '1':
            cnt_1 += 1

print(min(cnt_0, cnt_1))