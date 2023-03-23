def solution(s):
    stack=[]
    output=0
    multi=1

    for idx, c in enumerate(s):
        if c=='(':
            stack.append(c)
            multi*=2
        elif c=='[':
            stack.append(c)
            multi*=3
        elif c==')':
            if len(stack) == 0 or stack.pop() != '(':
                return 0
            if s[idx-1] == '(':
                output+=multi
            multi//=2
        elif c==']':
            if len(stack) == 0 or stack.pop() != '[':
                return 0
            if s[idx-1] == '[':
                output+=multi
            multi//=3

    if len(stack) != 0:
        return 0
    return output

_input = input()
print(solution(_input))