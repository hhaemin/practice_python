'''
조합 계산 모듈을 만들고 다음 조합 계산 결과를 출력해보자

8C3 = 56
7C5 = 21
'''

import combination as ct

numN = int(input('numN 입력:'))
numR = int(input('numR 입력:'))

print(f'{numN}C{numR}: {ct.getCombinationCnt(numN, numR)}')
