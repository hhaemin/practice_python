'''
1부터 100사이에 난수 10개를 생성한 후 짝수와 홀수를 구분해서 
리스트에 저장하고 각각의 개수를 출력하는 프로그램
'''

import random

randomList = random.sample(range(1, 101), 10)
evens = []
odds = []

for n in randomList:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

print(f'짝수: {evens}, 개수: {len(evens)}개')
print(f'홀수: {odds}, 개수: {len(odds)}개')
