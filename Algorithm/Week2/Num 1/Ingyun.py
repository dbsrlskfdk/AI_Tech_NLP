from collections import Counter
inp = input()
counter = Counter(sorted(list(inp)))

odd_num = 0
for alpha, num in counter.items():
    if num%2 == 1:
        odd_num += 1

if odd_num not in [0, 1]:
    print("I'm Sorry Hansoo")
else :
    left = ''
    midalpha = ''
    for alpha, num in counter.items():
        if num%2 == 0:
            left = left + alpha * (num//2)
        else :
            left = left + alpha * (num//2)
            midalpha = alpha
    print(left + midalpha + left[::-1])