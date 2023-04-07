import re

input1 = input()
input2 = input()

roma2num={"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1}
num2roma={1:["IX", "V", "IV", "I"], 2:["XC", "L", "XL", "X"], 3:["CM", "D", "CD", "C"], 4:["M"]}

arr1 = re.findall(r"CM|CD|XC|XL|IX|IV|[MDCLXVI]", input1)
arr2 = re.findall(r"CM|CD|XC|XL|IX|IV|[MDCLXVI]", input2)

num = sum([roma2num[key] for key in arr1]) + sum([roma2num[key] for key in arr2] )
print(num)

answer=[]
for i in range(1,5):
    idx = 0
    if num == 0:
        break
    n = num%10**i 
    num -= num%10**i #i=1)num=2493 -> num=2490, n=3 , i=2)num=2490 -> num=2400, n=90
    arr = []
    while n != 0:
        k = roma2num[num2roma[i][idx]]
        if n - k < 0:
            idx += 1
        elif n - k >= 0:
            n -= k
            arr.append(num2roma[i][idx])
    answer = arr + answer

print(''.join(answer))