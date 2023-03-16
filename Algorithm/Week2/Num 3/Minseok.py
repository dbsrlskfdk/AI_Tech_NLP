# https://www.acmicpc.net/problem/1439

string = input()

# 0과 1 각각 군집의 갯수를 저장하기 위한 배열.
list_count = [0, 0]

# 현재 카운트중인 군집
state = int(string[0])
list_count[state] += 1

# 배열을 돌아다니며 군집 세기.
for i in string[1:]:
	int_i = int(i)

	if int_i == state:
		continue
	else:
		state = int_i
		list_count[state] += 1

# 가장 적은 군집 출력
print(min(list_count))
