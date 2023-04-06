import re

n = int(input())
output1 = ["Protocol = ",'Host     = ','Port     = ','Path     = ']

for i in range(1, n+1):
    information = input()
    m = re.match(r'(\w+)://([\w.-]+)(?::(\d+))?(?:/(\S+))?', information)
    print(f'URL #{i}')
    output2 = ["<default>" if m.group(idx) == None else m.group(idx) for idx in range(1,5)]
    for o1, o2 in zip(*[output1, output2]):
        print(o1+o2)
    print()