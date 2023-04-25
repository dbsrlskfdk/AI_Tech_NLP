import re

K = int(input())
stop_word = r"()[]{}.,;:"
p = re.compile(r"(?<!\S)\w+(?!\S)")
def sub_word(x):
    if x in stop_word:
        x = " " + x + " "
        return x
    else:
        return x.lower()


for i in range(K):
    s1 = p.findall("".join(map(sub_word, input())))
    s2 = p.findall("".join(map(sub_word, input())))
    if s1 == s2:
        print(f"Data Set {i+1}: equal")
    else:
        print(f"Data Set {i+1}: not equal")
    print()