import re

T = int(input())
for _ in range(T):
    string = input()
    new = re.sub('^[ABCDEF]?A+F+C+[ABCDEF]?$', 'Infected!', string)
    
    print(new) if new == 'Infected!' else print('Good')