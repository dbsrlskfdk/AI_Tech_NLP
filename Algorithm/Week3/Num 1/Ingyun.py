old = list(input())
# old = list('(()[[]])([])')(()[[]])([])
# old = list('[][]((])')
good = {'()':'2', '[]':'3'}
# print(old) ####


new = []
flag = False
for i in range(len(old)):
    try :
        if old[i]+old[i+1] in good and flag==False:
            new.append(good[old[i]+old[i+1]])
            flag = True
        else :
            new.append(old[i])
            if flag:
                new.pop()
                flag = False
    except :
        new.append(old[i])
        if flag:
            new.pop()
            flag = False
# print(new, 111) #['(', '2', '[', '3', ']', ')', '(', '3', ')']



for _ in range(60):
    old = new
    new = []
    flag = 0
    for i in range(len(old)):
        try : 
            if old[i]+old[i+2] in good and flag==0:
                temp = int(old[i+1]) * int(good[old[i]+old[i+2]])
                new.append(str(temp))
                flag = 2
            else :
                new.append(old[i])
                if flag != 0 :
                    new.pop()
                    flag = flag - 1
        except :
            new.append(old[i])
            if flag != 0 :
                new.pop()
                flag = flag - 1
    # print(new) #['(', '2', '9', ')', '6']


    old = new
    new = []
    flag = 0
    for i in range(len(old)):
        try:
            if old[i].isdecimal() and old[i+1].isdecimal() and flag==0 :
                temp = int(old[i])+int(old[i+1])
                new.append(str(temp))
                flag = 1
            else :
                new.append(old[i])
                if flag == 1:
                    new.pop()
                    flag = 0
        except :
            new.append(old[i])
            if flag == 1:
                new.pop()
                flag = 0
    # print(new) #['(', '11', ')', '6']
# print(new)['28']

# print(new)
for what in new:
    if what.isdecimal() == False :
        print(0)
        break
else :
    print(int(new[0]))