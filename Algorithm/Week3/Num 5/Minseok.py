# https://www.acmicpc.net/problem/4659

# 단어와 성공여부
results = []

# 모음모음
list_aeiou = ["a", "e", "i", "o", "u"]

# text의 길이가 num_len과 같은 경우 True
def isLen(text, num_len):
	if len(text) == num_len:
		results.append([text, True])
		return True

	return False

# end 나올때까지 반복. 
while True:
	text = input()
	is_exit = True

	# END인 경우 종료
	if text == "end":
		break

	# CASE 1
	for i in list_aeiou:
		if i in text:
			is_exit = False
			break

	# 오류난 경우 실패 기록 후 다음단어 진행. 
	if is_exit:
		results.append([text, False, 1])
		continue

	# CASE 3
	if isLen(text, 1):
		continue

	for i in range(1, len(text)):
		char_1 = text[i - 1]
		char_2 = text[i]

		# 한 단어라도 e 혹은 o 인경우 pass. 
		if char_1 in ["e", "o"]:
			continue

		# 두 단어가 같은 경우(위의 case 제외) 오류 발생. 
		if char_1 == char_2:
			results.append([text, False, 3])
			is_exit = True
			break

	# 오류난 경우 다음단어 진행. 
	if is_exit:
		continue

	# CASE 2
	if isLen(text, 2):
		continue

	# 단어의 모음 여부를 기록 후 모두 True/False 여부 확인. 
	for i in range(2, len(text)):
		char_1 = text[i - 2] in list_aeiou
		char_2 = text[i - 1] in list_aeiou
		char_3 = text[i] in list_aeiou

		if char_1 == char_2 and char_2 == char_3:
			results.append([text, False, 2])
			is_exit = True
			break

	# 오류난 경우 다음단어 진행. 
	if is_exit:
		continue

	results.append([text, True])

# 출력
for i in results:
	print("<" + i[0] + "> is ", end="")
	if not i[1]:
		print("not ", end="")
	print("acceptable.")