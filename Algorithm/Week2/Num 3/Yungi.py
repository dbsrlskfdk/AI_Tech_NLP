S = input()

cons_char = ""
cons_char_dict = {'0':0, '1':0}
for c in S:
    if len(cons_char) == 0: # 연속된 글자가 없으면(시작일 때)
        cons_char += c
    elif cons_char[-1] == c: # 마지막에 글자가 이번에 순회할 글자와 같다면 => 연속이라는 것
        cons_char += c # 연속글자에 추가
    else: # 위에가 다 아니라면 연속이라는게 아니니까
        cons_char_dict[cons_char[-1]] += 1
        cons_char = c # 이번 글자를 연속글자의 시작으로
cons_char_dict[cons_char[-1]] += 1

print(min(cons_char_dict.values()))