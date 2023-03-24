# https://www.acmicpc.net/problem/5430

num_test_case = int(input())
arr_result = []

for i in range(num_test_case):
	commands = input()
	len_arr = int(input())
	# 잡다한거 지우고 배열로 변환
	arr = input().replace("[", "").replace("]", "").split(",")

	# 현재 역순 차례인가?
	# 뒤집은 횟수
	# 에러 발생했나?
	# 앞 뒤 지울 횟수.
	is_reverse = False
	is_error = False
	cnt_reverse = 0
	list_del = [0, 0]

	for command in commands:
		# 뒤집는 명령어의 경우.
		if command == "R":
			is_reverse = not is_reverse
			cnt_reverse += 1
			continue

		# 명령어가 D인데 지울게 없는경우 err.
		if len_arr == 0:
			is_error = True
			break

		# 현재 역순 상황에 따라 요소 삭제 - 구
		# pos = len(arr) - 1 if is_reverse else 0
		# del arr[pos]

		# 앞 혹은 뒤 지울 구간 추가 - 신
		if is_reverse:
			list_del[1] += 1
		else:
			list_del[0] += 1

		# 요소 갯수 줄이기.
		len_arr -= 1

	# 앞, 뒤 횟수만큼 잘라버리기.
	arr = arr[list_del[0]:len(arr) - list_del[1]]

	# 역순 횟수가 홀수번인 경우 뒤집기.
	if cnt_reverse % 2 == 1:
		arr = arr[::-1]

	# 에러 발생 여부에 따른 결과 반환.
	if is_error:
		arr_result.append("error")
	else:
		arr_result.append(arr)

for result in arr_result:
	print(str(result).replace("'", "").replace(" ", ""))
