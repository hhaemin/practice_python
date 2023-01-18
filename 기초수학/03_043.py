'''
<조합>
9C4, 6C2

카드 7장 중 3장을 선택했을 때 3,4,5가 동시에 선택될 수 있는 확률은?
'''

#9c4, 6c2
numN = int(input('numN 입력: '))
numR = int(input('numR 입력: '))
resultP = 1
resultR = 1
resultC = 1

for n in range(numN, (numN-numR), -1):
    print('n : {}'.format(n))
    resultP = resultP * n

print('resultP: {}'.format(resultP))

for n in range(numR, 0, -1):
    print('n : {}'.format(n))
    resultR = resultR * n

print('resultR: {}'.format(resultR))

resultC = int(resultP / resultR)
print('resultC: {}'.format(resultC))

# --------------------------------------
# result = 7C3
result = (1/resultC)*100
print('{}%'.format(round(result, 2)))