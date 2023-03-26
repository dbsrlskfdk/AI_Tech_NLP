from collections import deque

T = int(input())

ans = []
for _ in range(T):
    flag = 1
    p = input()
    n = int(input())
    test_arr = deque(input().removeprefix('[').removesuffix(']').split(','))

    if n == 0 and p.count('D') > 0:
        ans.append("error")
        n -= 1
    else:
        for i in range(len(p)):
            if p[i] == 'R':
                flag *= -1
            elif p[i] == 'D':
                if n > 0:
                    if flag == 1:
                        test_arr.popleft()
                        n -= 1
                    elif flag == -1:
                        test_arr.pop()
                        n -= 1
                else:
                    ans.append("error")
                    n -= 1
                    break

    if n >= 0:
        if flag == 1:
            ans.append("[" + ",".join(test_arr) + "]")
        elif flag == -1:
            test_arr.reverse()
            ans.append("[" + ",".join(test_arr) + "]")

for i in range(T):
    print(ans[i])