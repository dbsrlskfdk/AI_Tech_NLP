import re

def do_func(url):
    temp = re.split(r'://', url, 1)
    Protocol = temp[0]
    url = temp[1]

    temp = re.split(r':', url, 1)
    if temp[0] == url or '/' in temp[0]:
        # no Port
        temp = re.split(r'/', url, 1)
        if temp[0] == url:
            # no Path
            Host = temp[0]
            Port = '<default>'
            Path = '<default>'
            print('Protocol =', Protocol)
            print("Host     =", Host)
            print("Port     =", Port)
            print("Path     =", Path)
            return '_'
        Host = temp[0]
        Port = '<default>'
        Path = temp[1]
        print('Protocol =', Protocol)
        print("Host     =", Host)
        print("Port     =", Port)
        print("Path     =", Path)
        return '_'
    Host = temp[0]
    url = temp[1]

    temp = re.split(r'/', url, 1)
    if temp[0] == url:
        # no path
        Port = temp[0]
        Path = '<default>'
        print('Protocol =', Protocol)
        print("Host     =", Host)
        print("Port     =", Port)
        print("Path     =", Path)
        return '_'
    Port = temp[0]
    Path = temp[1]
    print('Protocol =', Protocol)
    print("Host     =", Host)
    print("Port     =", Port)
    print("Path     =", Path)
    return '_'

num = int(input())
for i in range(num):
    url = input()
    print(f"URL #{i+1}")
    do_func(url)
    print()



# import re
# output = ["Protocol = ",'Host     = ','Port     = ','Path     = ']
# for i in range(1, int(input())+1):
#     s = input()
#     p = re.match(r'(http|ftp|gopher)://([\w.-]+)(?::([\d]+))?(?:/([\S]+))?',s)
#     print(f"URL #{i}")
#     for j, k in enumerate(output,1):
#         print(f"{k}{p.group(j)}".replace("None","<default>"))
#     print()