task_len = int(input())
all_arr = []
min_pos = 2 ** 23 - 1
max_pos = 0
arr = [0] * (2 ** 23 - 1)

for i in range(task_len):
    start, end = input().split(" ")
    start, end = int(start), int(end)
    # arr[start] = -1
    arr[end] = end - start
    # all_arr.append([start, end])
    min_pos = end if min_pos > end else min_pos
    max_pos = end if max_pos < end else max_pos

res = 0
cnt = 0

print(arr[:max_pos + 1])
for i in arr[min_pos:max_pos + 1]:
    print(i, res)
    if i != 0 and res == 0:
        res = i - 1
        cnt += 1
        continue

    res -= 1

print(cnt)
