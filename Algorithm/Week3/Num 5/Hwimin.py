def f(string):
    #1번 조건
    if not [word for word in string if word in ['a','e','i','o','u']]:
        return False
    
    #2번 조건
    cnt1=0
    cnt2=0
    for word in string:
        if word in ['a','e','i','o','u']:
            cnt1=0
            cnt2+=1
        else:
            cnt1+=1
            cnt2=0
        if cnt1==3 or cnt2==3:
            return False
    
    #3번 조건
    stack=[]
    for word in string:
        if stack and word!='e' and word!='o':
            if stack.pop() == word:
                return False
        stack.append(word)
    return True

s = input()
while s != 'end':
    if f(s):
        print(f'<{s}> is acceptable.')
    else:
        print(f'<{s}> is not acceptable.')
    s = input()