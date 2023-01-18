'''
소인수와 소인수분해
100부터 1000사이의 난수를 소인수분해를 하고 각각의 소인수에 대한 지수를 
출력하는 프로그램

ex. 20의 소인수분해 : 2 * 2 * 5 -> 2, 1
'''

import random

rNum = random.randint(100, 1000)
print(f'rNum: {rNum}')

soinsuList = []

n = 2
while n <= rNum:
    if rNum % n == 0:
        print(f'소인수: {n}')
        soinsuList.append(n)            # 배열에 소인수를 하나씩 추가
        rNum /= n
    else:
        n += 1

print(f'soinsuList: {soinsuList}')

tempNum = 0
for s in soinsuList:
    if tempNum != s:
        print(f'{s}\'s count: {soinsuList.count(s)}')
        tempNum = s