bracket = [i for i in input()]
stack = []

def f(bracket, stack):
    while bracket:
        pop_bracket = bracket.pop(0)

        if pop_bracket == ")": # 닫는 괄호가 나올 시
            if stack[-1] == "(": # 마지막 괄호가 여는 괄호면
                stack.pop() # 빼고
                stack.append(2) # 2 대입
            elif type(stack[-1]) == int: # 마지막 괄호가 숫자면,
                tmp = stack.pop() # 마지막 숫자 뽑고 ==> int니까
                if len(stack) != 0:
                    t = stack[-1] # 마지막 수 확인
                    while type(t) == int: # 만약 또 int형이면
                        tmp += stack.pop() # 마지막 수 더해준다.
                        t = stack[-1]

                    stack.pop() # 문자는 뽑아주고
                    tmp *= 2 # 2곱해주고
                    stack.append(tmp) # 다시 stack에 마지막에 추가해준다.
        elif pop_bracket == "]":
            if stack[-1] == "[":
                stack.pop()
                stack.append(3)
            elif type(stack[-1]) == int:
                tmp = stack.pop()
                if len(stack) != 0:
                    t = stack[-1]
                    while type(t) == int:
                        tmp += stack.pop()
                        t = stack[-1]

                    stack.pop()
                    tmp *= 3
                    stack.append(tmp)
        else:
            stack.append(pop_bracket)
    return sum(stack)

check_stack = []
check = False
for i in bracket:
    if i == "(" or i == "[":
        check_stack.append(i)
    if i == ")":
        if len(check_stack) != 0 and check_stack[-1] == "(":
            check_stack.pop()
        else:
            check = False
            check_stack.append(i)
            break
    if i == "]":
        if len(check_stack) != 0 and check_stack[-1] == "[":
            check_stack.pop()
        else:
            check = False
            check_stack.append(i)
            break
if len(check_stack) == 0:
    check = True
if check:
    print(f(bracket, stack))
else:
    print(0)