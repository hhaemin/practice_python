'''
박스에 '꽝'이 적힌 종이가 6장 있고, '선물'이 적힌 종이가 4장이 있을떄,
꽝 3장과 선물 3장을 뽑는 확률은?
'''
# 6C3 * 4C3 / 10C6

def proFun():
    numN = int(input('numN 입력: '))
    numR = int(input('numR 입력: '))
    resultP = 1
    resultR = 1
    resultC = 1

# 순열 P
    for n in range(numN, (numN-numR), -1):
        resultP = resultP * n
    print('resultP: {}'.format(resultP))

# R : factorial
    for n in range(numR, 0, -1):
        resultR = resultR * n
    print('resultR: {}'.format(resultR))

# 조합 C
    resultC = int(resultP / resultR)
    print('resultC: {}'.format(resultC))

    return resultC

sample = proFun()
print('sample: {}'.format(sample))

event1 = proFun()
print('event1: {}'.format(event1))

event2 = proFun()
print('event2: {}'.format(event2))

probability = (event1 * event2) / sample
print('probability: {}%'.format(round(probability * 100, 2)))