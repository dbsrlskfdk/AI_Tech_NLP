from collections import defaultdict

word = input()
vocab_cnt = defaultdict(int)
for w in word:
    vocab_cnt[w] += 1
vocab_cnt = dict(sorted(vocab_cnt.items(), key=lambda x: x[0]))

res = ""
center_char = ""
odd_cnt = 0
if len(word) % 2 == 0:
    for i in vocab_cnt.values():
        if i % 2 != 0:
            odd_cnt += 1
    if odd_cnt > 1:
        res = "I'm Sorry Hansoo"
    else:
        for k, i in vocab_cnt.items():
            res += k * (i // 2)
        res += res[::-1]
else:
    for k, i in vocab_cnt.items():
        if i % 2 != 0:
            odd_cnt += 1
            center_char = k
    if odd_cnt > 1:
        res = "I'm Sorry Hansoo"
    else:
        for k, i in vocab_cnt.items():
            res += k * (i // 2)
        res += center_char
        res += res[::-1][1:]

print(res)