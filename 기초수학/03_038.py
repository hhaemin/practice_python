'''
<시그마>
첫 째날 쌀 두톨을 받고 둘째 날부터는 하루 전의 2배의 해당하는 쌀을 받는다고 할 때,
30일째 되는 날 받게 되는 쌀의 개수를 수열과 시그마로 나타내고 이를 출력하는 프로그램
{2, 4, 8, 16, 32, 64, 128, ...} -> 시그마 문제지만, 등비수열과 같은 맥락
'''

inputA1 = int(input('a1 입력: '))
inputR = int(input('공비 입력: '))
inputN = int(input('n 입력: '))

valueN = 0
sumN = 0
n = 1
while n <= inputN:

    if n == 1:
        valueN = inputA1
        sumN += valueN
        print('{}번째 항까지의 합: {}'.format(n, sumN))
        n += 1
        continue

    valueN *= inputR
    sumN += valueN
    print('{}번째 항까지의 합: {}'.format(n, sumN))
    n += 1

print('{}번째 항까지의 합: {}'.format(inputN, format(sumN,',')))


# 등비 수열(합) 공식: sn = a1 * (1 - r^n) / (1-r)
sumN = inputA1 * (1 - (inputR ** inputN)) / (1 - inputR)
print('{}번째 항까지의 합: {}'.format(inputN, int(sumN)))
