# https://www.acmicpc.net/problem/1213

char_input = input()
char_count = {}

# 알파벳별 출현 횟수 카운트. 
for i in char_input:
	if i in char_count:
		char_count[i] += 1
		continue

	char_count[i] = 1

# 각 알파벳별 출현 횟수에 대해 알파벳 순으로 정렬. 
char_count = {key: value for key, value in sorted(char_count.items())}

# palindrome - CENTRT - palindrome.reverse
# 위의 방식으로 출력
# res 			: 양 변에 출력하고 남은 문자 갯수. 
# center		: 양 변에 출력하고 남은 문자. 
# palindrome	: 양 변에 출력 할 문자. 
res = 0
center = ""
palindrome = ""

for i in char_count:
	# 양변에 2로 나누어 떨어진 만큼 문자 저장. 
	palindrome = palindrome + (i * int(char_count[i] / 2))
	
	# 해당 알파벳이 양 변에 출력 후 남는 문자가 없는 경우 continue. 
	if char_count[i] % 2 == 0:
		continue

	# 남은 문자가 2개 이상인 경우 오류 메세지 출력 후 종료. 
	res += 1
	if res > 1:
		print("I'm Sorry Hansoo")
		break

	center = i

# 모두 수행한 경우 펠린드롬 출력. 
if not (res > 1):
	print(palindrome + center + palindrome[::-1])