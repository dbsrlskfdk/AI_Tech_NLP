import re
pw = input()
while pw != 'end':
    if len(re.findall("[aeiou]", pw)) != 0 and (len(re.findall("[aeiou]{3,}", pw)) == 0 and len(re.findall("[^aeiou]{3,}", pw)) == 0) and len(re.findall(r"([^eo])\1", pw)) == 0:
        print(f"<{pw}> is acceptable.")
    else:
        print(f"<{pw}> is not acceptable.")
    pw = input()