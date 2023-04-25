import re
for _ in range(int(input())):
    print("Infected!") if len(re.findall(r"^[A-F]?A+F+C+[A-F]?$", input())) != 0 else print("Good")