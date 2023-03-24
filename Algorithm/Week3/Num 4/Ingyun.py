def do_test():
    ps = input()
    num = input()
    input_ = input()
    if input_ == '[]':
        arr = []
    else : 
        arr = list(map(int, input_[1:-1].split(',')))

    now = 'go'
    arr = deque(arr)
    for p in ps:
        if p == 'R':
            if now=='go':
                now = 'back'
            elif now=='back' :
                now = 'go'
        elif p == 'D' :
            if len(arr)==0:
                print('error')
                break
            #################
            if now=='go':
                arr.popleft()
            elif now=='back':
                arr.pop()
        # print(arr)
    else :
        if now=='go':
            print(str(list(arr)).replace(' ',''))
        elif now=='back':
            print(str(list(arr)[::-1]).replace(' ',''))
            

T = int(input())
from collections import deque
for _ in range(T):
    do_test()