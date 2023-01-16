'''
순열 계산 모듈을 만들고 다음 순열 계산 결과를 출력해보자

8P3 = 336
7P5 = 2520
'''

import permutation as pt

numN = int(input('numN 입력: '))
numR = int(input('numR 입력: '))

print(f'{numN}P{numR}: {pt.getPermutationCnt(numN, numR)}')

# getPermutation 함수 사용시, 항목을 다 확인할 수 있음.
#listVar = [1,2,3,4,5,6,7,8]
#rVar = 3
#pt.getPermutations(listVar, rvar)
#print(f'{numN}P{numR}: {pt.getPermutationCnt(numN, numR)}')