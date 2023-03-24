from collections import deque
N = int(input())
for i in range(N):
    s=input().replace('RR','')
    n=int(input())
    arr=input()
    dq=deque(arr[1:-1].split(',')) if n != 0 else deque([])
    _reverse=0
    for c in s:
        if c == 'R':
            _reverse+=1
            _reverse%=2
        elif c == 'D' and dq:
            if _reverse == 0:
                dq.popleft()
            elif _reverse == 1:
                dq.pop()
        else:
            print('error')
            break
    else:
        if _reverse == 1:
            dq.reverse()
        print("["+",".join(dq)+"]")
            
    